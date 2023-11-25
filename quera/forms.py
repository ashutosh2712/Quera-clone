from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer


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


class QuestionForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "post-text-ques",
                "rows": 10,
                "cols": 75,
                "placeholder": "Enter your question here...",
            }
        )
    )

    class Meta:
        model = Question
        fields = ["content"]


class AnswerForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "post-text-ans",
                "rows": 10,
                "cols": 100,
                "placeholder": "Write your answer...",
            }
        ),
        required=True,
    )

    class Meta:
        model = Answer
        fields = ["content"]
