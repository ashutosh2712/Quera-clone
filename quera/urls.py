from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("postques/", views.postques, name="postques"),
    path("postans/", views.postans),
]
