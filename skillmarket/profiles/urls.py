from django.urls import path
from . import views

urlpatterns = [
    path("<slug:username>/", views.UserView.as_view(), name = "profile")
]