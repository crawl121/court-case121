from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path("register/", views.register_user, name="register"),

    # viewing for displaying
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
     
]