from django.urls import path, register_converter
from . import views

urlpatterns = [
    path("<username:user>/", views.UserView.as_view(), name = "profile")
]