from accounts.models import User
u = User.objects.get(email='raphaelmazini37@gmail.com')
u.staff = True
u.admin = True
u.is_superuser = True
u.save()
exit()