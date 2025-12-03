from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import FreelanceUser


@admin.register(FreelanceUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "usable_password", "password1", "password2", 'role'),
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('phone', 'role')}),
    )
