from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

class RegisterForm(forms.Form):
    full_name = forms.CharField(label="Nome Completo")
    email     = forms.EmailField(label="E-mail")
    password  = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def clean(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password2'):
            raise forms.ValidationError("As senhas devem ser iguais.")
        return data

class GuestForm(forms.Form):
    email = forms.EmailField(label="E-mail para convidado")