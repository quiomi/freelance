from django.db import models
from accounts.models import FreelanceUser


def user_directory_path(instance, filename):
    return 'avatar/user_{0}/{1}'.format(instance.user.id, filename)

class SellerUser(models.Model):
    user = models.OneToOneField(FreelanceUser, on_delete=models.CASCADE, related_name='seller_profile')
    
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    orders = models.PositiveIntegerField(default=0)
    reviews_all = models.PositiveIntegerField(default=0)
    positive_reviews = models.PositiveIntegerField(default=0)
    negative_reviews = models.PositiveIntegerField(default=0)
    orders_completed = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    
    skills = models.ManyToManyField('Skill', blank=True, related_name='sellers')
    reviews = models.ManyToManyField('Review', blank=True, related_name='sellers')
    

class Review(models.Model):
    reviewer = models.ForeignKey(FreelanceUser, on_delete=models.CASCADE, related_name='given_reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Skill(models.Model):
    name = models.CharField(max_length=100)