from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin # Adicione PermissionsMixin aqui
)

class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)
    def create_user(self, email, password = None, is_active = True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError("O Usuário deve ter um endereço de email.")
        if not password:
            raise ValueError("O Usuário deve ter uma senha.")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) # muda a senha
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self, email, password = None):
        user = self.create_user(
            email,
            password = password,
            staff = True
        )
        return user
    def create_superuser(self, email, password = None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True,
            is_admin = True,
        )
        return user
class User(AbstractBaseUser, PermissionsMixin): # Adicione aqui também
    email       = models.EmailField(max_length=255, unique=True)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email