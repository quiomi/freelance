from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SellerUser, BuyerUser
from accounts.models import FreelanceUser


@receiver(post_save, sender = FreelanceUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'Seller':
            SellerUser.objects.create(user=instance)
        elif instance.role == 'Buyer':
            BuyerUser.objects.create(user=instance)