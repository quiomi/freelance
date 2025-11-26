from django.shortcuts import render
from django.views.generic.detail import DetailView
from accounts.models import FreelanceUser
from django.http import HttpRequest

# Create your views here.

class UserView(DetailView):
    model = FreelanceUser
    template_name = "profiles/profile.html"
    slug_url_kwarg = 'username'
    slug_field = 'username'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context