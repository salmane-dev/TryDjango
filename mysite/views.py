from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, let's get started!")

def page2(request):
    return HttpResponse("Hello, Wellkomen zu page II")
