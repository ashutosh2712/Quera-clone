from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("login/", views.login),
    path("signup/", views.signup),
    path("postques/", views.postques),
    path("postans/", views.postans),
]
