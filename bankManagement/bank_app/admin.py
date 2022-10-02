from django.contrib import admin
from .models import UserProfile, Bank

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Bank)