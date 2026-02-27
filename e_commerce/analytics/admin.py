from django.contrib import admin
from .models import ObjectViewed
from .models import UserSession
admin.site.register(ObjectViewed)
admin.site.register(UserSession)