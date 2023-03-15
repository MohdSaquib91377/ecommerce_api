from django.urls import path
from account.api import views as account_views
urlpatterns = [
    path("register/",account_views.UserRegistrationView.as_view()),
    path("login/",account_views.LoginView.as_view()),
    path("send-otp/",account_views.SendOTpView.as_view())

]