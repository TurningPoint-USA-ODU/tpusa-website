from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def events(request: HttpRequest) -> HttpResponse:
    return render(request, "main/events.html")


def join(request: HttpRequest) -> HttpResponse:
    return render(request, "main/join.html")


def leadership(request: HttpRequest) -> HttpResponse:
    return render(request, "main/leadership.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "main/contact.html")
