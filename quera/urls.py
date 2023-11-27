from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("postques/", views.postques, name="postques"),
    path("postans/<int:question_id>/", views.postans, name="postans"),
    path("upvote/<int:answer_id>/", views.upvote, name="upvote"),
    path("downvote/<int:answer_id>/", views.downvote, name="downvote"),
]
