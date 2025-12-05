from django.test import TestCase
from accounts.models import FreelanceUser
from accounts.forms import RegistrationForm, LoginForm
from django.urls import reverse

    
class TestLogin(TestCase):
    def setUp(self):
        self.valid_data_test = {
            "username": "loraels",
            "email": "ldt@gmail.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
            "role": "Buyer",
            "country": "Germany"
        }
        form = RegistrationForm(self.valid_data_test)
        if form.is_valid():
            form.save()
            
    def test_correct_email(self):
        data = {
            "username": "ldt@gmail.com",
            "password": "StrongPassword123!"
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())
        data["username"] = "loraels"
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())