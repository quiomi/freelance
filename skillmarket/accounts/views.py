from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .forms import LoginView
from django.contrib.auth import login

# Create your views here.


def auth_login(request: HttpRequest):
    if request.method == "POST":
        form = LoginView(request, data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            data = {'status': True, 'redirect_url': f'http://127.0.0.1:8000/user/{user.username}/'}
            return JsonResponse(data)
        data = {'status': False}
        print(form.errors.items())
        return JsonResponse(data)
    return render(request, 'accounts/login.html')
    