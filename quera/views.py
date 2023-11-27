from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm, QuestionForm, AnswerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Question, Answer, Vote


# Create your views here.
@login_required(login_url="login")
def home(request):
    questions = (
        Question.objects.annotate(
            upvote_count=Count(
                "answers__votes", filter=Q(answers__votes__vote_type="upvote")
            )
        )
        .all()
        .order_by("-created_at")
    )
    form = QuestionForm()
    ans_form = AnswerForm()

    for question in questions:
        for answer in question.answers.all():
            answer.upvotes = answer.votes.filter(vote_type="upvote").count()

    context = {"form": form, "questions": questions, "ans_form": ans_form}
    return render(request, "homepage.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was Created for " + user)
                return redirect("home")

        context = {"form": form}
        return render(request, "signup.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or Password is incorrect")

        context = {}
        return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def postques(request):
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect("home")
        else:
            errors = form.errors

    context = {"form": form, "errors": errors}
    return render(request, "homepage.html", context)


def postans(request, question_id):
    question = Question.objects.get(pk=question_id)
    ans_form = AnswerForm()
    if request.method == "POST":
        ans_form = AnswerForm(request.POST)
        if ans_form.is_valid():
            answer = ans_form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect("home")
    else:
        errors = ans_form.errors
    context = {"ans_form": ans_form, "errors": errors, "question": question}
    return render(request, "homepage.html", context)


def upvote(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    user = request.user
    existing_vote = Vote.objects.filter(user=user, answer=answer).first()

    if existing_vote:
        existing_vote.delete()
    else:
        Vote.objects.create(user=request.user, answer=answer, vote_type="upvote")

    # updated_upvotes_count = answer.votes.filter(vote_type="upvote").count()
    answer.upvotes = answer.votes.filter(vote_type="upvote").count()
    answer.downvotes = answer.votes.filter(vote_type="downvote").count()
    answer.save()
    print(answer.upvotes)

    return JsonResponse({"upvotes": answer.upvotes})


def downvote(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    user = request.user
    existing_vote = Vote.objects.filter(user=user, answer=answer).first()

    if existing_vote:
        existing_vote.delete()
    else:
        Vote.objects.create(user=request.user, answer=answer, vote_type="downvote")

    updated_downvotes_count = answer.votes.filter(vote_type="downvote").count()
    return JsonResponse({"downvotes": updated_downvotes_count})
