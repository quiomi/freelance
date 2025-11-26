from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class FreelanceUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    class UserRole(models.TextChoices):
        SELLER = 'Seller'
        BUYER = 'Buyer'
    
    role = models.CharField(max_length=6, choices=UserRole.choices)
