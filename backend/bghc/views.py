from directory.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views import generic


class BghcLoginView(LoginView):
    template_name = "bghc/login.html"
    next_page = "/bghc/dashboard/"


class BghcSignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("bghc_login")
    template_name = "bghc/signup.html"


def dashboard(request: HttpRequest):
    return HttpResponse("The Black Girl Health Collective Dashboard")


def index(request: HttpRequest):
    context = {"author": "Travis"}
    return render(request, template_name="bghc/index.html", context=context)
