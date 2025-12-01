from django.db import models
from accounts.models import FreelanceUser


def user_directory_path(instance, filename):
    return 'avatar/user_{0}/{1}'.format(instance.user.id, filename)

class SellerUser(models.Model):
    user = models.OneToOneField(FreelanceUser, on_delete=models.CASCADE, related_name='seller_profile')
    
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name="Avatar user image")
    description = models.TextField(null=True, blank=True, verbose_name="Description about seller")
    orders = models.PositiveIntegerField(default=0, verbose_name="Total number of orders")
    reviews_all = models.PositiveIntegerField(default=0, verbose_name="Total number of reviews")
    positive_reviews = models.PositiveIntegerField(default=0, verbose_name="Number of positive reviews")
    negative_reviews = models.PositiveIntegerField(default=0, verbose_name="Number of negative reviews")
    orders_completed = models.PositiveIntegerField(default=0, verbose_name="Number of completed orders")
    
    skills = models.ManyToManyField('Skill', blank=True, related_name='sellers')
    
    class Meta:
        verbose_name = "Seller User Profile"
        verbose_name_plural = "Seller User Profiles"
        
        
    def __str__(self):
        return self.user.username


class Review(models.Model):
    reviewer = models.ForeignKey(FreelanceUser, on_delete=models.CASCADE, related_name='given_reviews', verbose_name="Reviewer")
    seller = models.ForeignKey(SellerUser, on_delete=models.CASCADE, related_name='reviews', verbose_name="Reviewed Seller")
    is_positive = models.BooleanField(verbose_name="Is Positive Review")
    comment = models.TextField(verbose_name="Review Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Review Created At")
    
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
    
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill")
    
    def __str__(self):
        return self.name