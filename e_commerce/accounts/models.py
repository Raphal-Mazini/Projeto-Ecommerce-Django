from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("O Usuário deve ter um endereço de email.")
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        user.is_superuser = True 
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(max_length=255, unique=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
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