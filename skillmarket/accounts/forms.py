from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import FreelanceUser
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label = "Email пользователя")
    
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email пользователя")
    role = forms.ChoiceField(choices=FreelanceUser.UserRole.choices, widget=forms.RadioSelect, label="Роль пользователя")
    
    class Meta:
        model = FreelanceUser
        fields = ('username', 'email', 'password1', 'password2', "role", "country")