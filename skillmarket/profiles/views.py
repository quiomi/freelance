from django.shortcuts import render
from django.views.generic.detail import DetailView
from accounts.models import FreelanceUser
from django.http import HttpRequest

# Create your views here.

class UserView(DetailView):
    model = FreelanceUser
    slug_url_kwarg = 'username'
    slug_field = 'username'
    
    
    
    def get_template_names(self):
        user: FreelanceUser = self.object
        if user.role == 'Seller':
            return ['profiles/seller_profile.html']
        else:
            return ['profiles/buyer_profile.html']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user: FreelanceUser = self.object
        if user.role == 'Seller':
            context['seller_profile'] = user.seller_profile
            scope = 0
            if user.seller_profile.orders_completed != 0 or user.seller_profile.orders != 0:
                scope = round((user.seller_profile.orders_completed / user.seller_profile.orders) * 5, 1)
                
            context["scope"] = scope
        return context