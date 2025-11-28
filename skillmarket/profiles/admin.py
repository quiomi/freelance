from django.contrib import admin
from .models import SellerUser, Skill

# Register your models here.
admin.site.register(SellerUser)
admin.site.register(Skill)