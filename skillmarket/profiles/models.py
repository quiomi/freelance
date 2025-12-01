from django.db import models
from accounts.models import FreelanceUser
from django.core.exceptions import ValidationError

def user_directory_path(instance, filename):
    return 'avatar/user_{0}/{1}'.format(instance.user.id, filename)


class BuyerUser(models.Model):
    user = models.OneToOneField(FreelanceUser, on_delete=models.CASCADE, related_name='buyer_profile')
    
    def clean(self):
        if self.user.role and self.user.role != 'Buyer':
            raise ValidationError("Пользователь уже имеет другую роль.")
        return super().clean()
    
    def save(self, *argv, **kwargv):
        self.full_clean()
        if self.user.role != "Buyer":
            raise ValidationError("User role must be 'Buyer' to create a BuyerUser profile.")
        return super().save(*argv, **kwargv)
    
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name="Avatar user image")
    description = models.TextField(null=True, blank=True, verbose_name="Description about buyer", max_length=1500)
    orders = models.PositiveIntegerField(default=0, verbose_name="Total number of orders")
    title = models.CharField(null=True, blank=True, verbose_name="Title", max_length=50)
    
    def __str__(self):
        return self.user.username


class SellerUser(models.Model):
    user = models.OneToOneField(FreelanceUser, on_delete=models.CASCADE, related_name='seller_profile')
    
    def clean(self):
        if self.user.role and self.user.role != 'seller':
            raise ValidationError("Пользователь уже имеет другую роль.")
        return super().clean()
    
    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if self.user.role != "Seller":
            raise ValueError("User role must be 'Seller' to create a SellerUser profile.")
        return super().save(force_insert, force_update, using, update_fields)
    
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name="Avatar user image")
    description = models.TextField(null=True, blank=True, verbose_name="Description about seller", max_length=1500)
    orders = models.PositiveIntegerField(default=0, verbose_name="Total number of orders")
    reviews_all = models.PositiveIntegerField(default=0, verbose_name="Total number of reviews")
    positive_reviews = models.PositiveIntegerField(default=0, verbose_name="Number of positive reviews")
    negative_reviews = models.PositiveIntegerField(default=0, verbose_name="Number of negative reviews")
    orders_completed = models.PositiveIntegerField(default=0, verbose_name="Number of completed orders")
    title = models.CharField(null=True, blank=True, verbose_name="Title", max_length=50)
    
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