from django.contrib import admin
from django_full_kit.django_full_kit.admin import AdvancedUserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(AdvancedUserAdmin):
    pass