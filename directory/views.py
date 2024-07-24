from django.http.request import HttpRequest
from django.http.response import HttpResponse


def index(request: HttpRequest):
    return HttpResponse("The Directory Application")
