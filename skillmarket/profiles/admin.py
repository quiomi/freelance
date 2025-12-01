from django.contrib import admin
from .models import SellerUser, Skill, Review

# Register your models here.
admin.site.register(SellerUser)
admin.site.register(Skill)
admin.site.register(Review)