from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "homepage.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def postques(request):
    return render(request, "postques.html")


def postans(request):
    return render(request, "postans.html")
