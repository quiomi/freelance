from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

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
    