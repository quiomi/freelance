from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login
from dotenv import load_dotenv
from .utils import get_ip
import requests
import os

# Create your views here.


def auth_login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='accounts.backends.EmailAuthBackend')
            data = {'status': True, 'redirect_url': f'/user/{user.username}/'}
            return JsonResponse(data)
        data = {'status': False}
        return JsonResponse(data)
    return render(request, 'accounts/login.html')
    
    
def auth_register(request: HttpRequest):
    if request.method == "POST":
        load_dotenv()
        
        request.META['HTTP_X_FORWARDED_FOR'] = '66.151.40.43'
        token = os.environ.get('TOKEN_IPINFO')
        ip = get_ip(request)
        url = f"https://api.ipinfo.io/lite/{ip}?token={token}"
        response = requests.get(url).json()
        
        
        data_copy = request.POST.copy()
        data_copy["country"] = response["country"]
        form = RegistrationForm(data_copy or None)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='accounts.backends.EmailAuthBackend')
            return  redirect('profile', user.username)
        print(form.data)
        print(form.errors)
    return render(request, 'accounts/registration.html')