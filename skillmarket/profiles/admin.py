from django.contrib import admin
from .models import SellerUser, Skill, Review, BuyerUser

# Register your models here.
admin.site.register(SellerUser)
admin.site.register(Skill)
admin.site.register(Review)
admin.site.register(BuyerUser)