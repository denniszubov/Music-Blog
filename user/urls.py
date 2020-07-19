from django.urls import path
from .views import register, profile
from django.contrib.auth import views as user_views

urlpatterns = [
    path("register/", register, name="user-register"),
    path("login/", user_views.LoginView.as_view(template_name="user/login.html"), name="user-login"),
    path("logout/", user_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),
    path("profile/", profile, name="user-profile"),
]
