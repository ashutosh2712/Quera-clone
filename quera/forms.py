from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "custom-class", "placeholder": "Username"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "custom-class", "placeholder": "Email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "custom-class", "placeholder": "Your Password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "custom-class", "placeholder": "Confirm your password"}
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
