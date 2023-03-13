from django.urls import path
from account import api as account_api
urlpatterns = [
    path("register/",account_api.UserRegistrationView.as_view())
]