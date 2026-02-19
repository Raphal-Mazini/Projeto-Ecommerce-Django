from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
# Esta é a função correta para versões atuais do Django
from django.utils.http import url_has_allowed_host_and_scheme 
from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail

User = get_user_model()

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
            return redirect(redirect_path)
        return redirect("/register/")
    return redirect("/register/")

def login_page(request):
    form = LoginForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        # No authenticate, passamos o email para o parâmetro 'username'
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
                return redirect(redirect_path)
            return redirect("/")
        else:
            print("Login inválido")
            
    return render(request, "accounts/login.html", {"form": form})

def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        full_name = form.cleaned_data.get("full_name")
        email     = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        User.objects.create_user(email, full_name=full_name, password=password)
        return redirect("/login/")
    return render(request, "accounts/register.html", {"form": form})

def logout_page(request):
    logout(request)
    return redirect("/login/")