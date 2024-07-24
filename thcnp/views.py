from django.contrib.auth.views import LoginView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views import generic

from directory.forms import CustomUserCreationForm


class ThcnpLoginView(LoginView):
    template_name = "thcnp/login.html"
    next_page = "/thcnp/dashboard/"


class ThcnpSignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("thcnp_login")
    template_name = "thcnp/signup.html"


def dashboard(request: HttpRequest):
    return HttpResponse(gettext("The Healthcare Navigation Project Dashboard"))


def index(request: HttpRequest):
    return HttpResponse(gettext("The Healthcare Navigation Project"))
