from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello")


def error(request):
    return HttpResponse("error 404")
