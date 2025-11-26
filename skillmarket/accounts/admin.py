from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import FreelanceUser


@admin.register(FreelanceUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('phone', 'role')}),
    )
