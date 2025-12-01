from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label = "Email пользователя")
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)