from django.contrib import admin
from .models import Cart

# User deve ser registado APENAS no admin.py de accounts
admin.site.register(Cart)