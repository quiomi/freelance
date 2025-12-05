from django.test import TestCase
from ..forms import RegistrationForm
from accounts.models import FreelanceUser
from django.urls import reverse

# Create your tests here.

class TestRegistration(TestCase):    
    def setUp(self):
        self.valid_data = {
            "username": "testuser",
            "email": "lefadft@gmail.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
            "role": "Buyer",
            "country": "Germany"
        }
        
        self.valid_data_test = {
            "username": "lorael",
            "email": "lddgdt@gmail.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
            "role": "Buyer",
            "country": "Germany"
        }
        form = RegistrationForm(data = self.valid_data_test)
        form.save()
    
    def AssertInvalidField(self, field: str, value: str):
        data = self.valid_data.copy()
        data[field] = value
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn(field, form.errors)
        fields = data.keys()
        for i in fields:
            if i != field:
                self.assertNotIn(i, form.errors)
        
                
    def AssertCorrectField(self, field: str, value: str):
        data = self.valid_data.copy()
        data[field] = value
        form = RegistrationForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_lol(self):
        self.valid_data_test2 = {
            "username": "loraelfsdf",
            "email": "lddasfdfdgdt@gmail.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
            "role": "Buyer",
            "country": "Germany"
        }
        form = RegistrationForm(data = self.valid_data_test2)
        self.assertTrue(form.is_valid())
        
    def test_correct_role(self):
        self.AssertCorrectField("role", "Buyer")
        self.AssertCorrectField("role", "Seller")
        
    def test_invalid_role(self):
        self.AssertInvalidField("role", "Buyer\n")
        self.AssertInvalidField("role", "Seller\n")
        self.AssertInvalidField("role", "buyer")
        self.AssertInvalidField("role", "seller")
        self.AssertInvalidField("role", "")
        self.AssertInvalidField("role", "Seller ")
        self.AssertInvalidField("role", "BuYer")
        self.AssertInvalidField("role", "Buyer ")
        self.AssertInvalidField("role", "Seller"*6)
        self.AssertInvalidField("role", "\nSeller")
        self.AssertInvalidField("role", "Sel\nler")
        self.AssertInvalidField("role", "\nBuyer")
    
    def test_correct_username(self):
        self.AssertCorrectField("username", "New_User")
        self.AssertCorrectField("username", "neW_uWe_f")
        self.AssertCorrectField("username", "testt")
        self.AssertCorrectField("username", "d_r_t_t")
        self.AssertCorrectField("username", "r4_43")
        self.AssertCorrectField("username", "r4r_3")
        self.AssertCorrectField("username", "a"*32)
        self.AssertCorrectField("username", "b"*5)
        self.AssertCorrectField("username", "a_a"*10)
        self.AssertCorrectField("username", "hellon\n")
    
    def test_invalid_username(self):
        self.AssertInvalidField("username", "lorael")
        self.AssertInvalidField('username', "Invalid@Username!")
        self.AssertInvalidField("username", "test")
        self.AssertInvalidField('username', "ab")
        self.AssertInvalidField('username', "")
        self.AssertInvalidField("username", "_"*32)
        self.AssertInvalidField('username', "a"*33)
        self.AssertInvalidField('username', "user name")
        self.AssertInvalidField('username', "user\nname")
        self.AssertInvalidField('username', "user\tname")
        self.AssertInvalidField('username', "user,name")
        self.AssertInvalidField('username', "user.name")
        self.AssertInvalidField('username', "user/name")
        self.AssertInvalidField('username', "user\\name")
        self.AssertInvalidField('username', "user@name")
        self.AssertInvalidField('username', "user_name"*33)
        self.AssertInvalidField('username', "root__")
        self.AssertInvalidField('username', "root_")
        self.AssertInvalidField("username", '_root')
        self.AssertInvalidField('username', 'ro__out')
        self.AssertInvalidField('username', '98root')
        self.AssertInvalidField("username", "324354")
        self.AssertInvalidField('username', '?clean')
        self.AssertInvalidField('username', 'fame')
        self.AssertInvalidField('username', '\nfame')
        
    