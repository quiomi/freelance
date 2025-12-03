from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login

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
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='accounts.backends.EmailAuthBackend')
            return  redirect('profile', user.username)
        print(form.data)
        print(form.errors)
    return render(request, 'accounts/registration.html')