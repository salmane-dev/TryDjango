from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    x = []  
    for i in range(10):
        x.append(i)
    return HttpResponse("<center><h1>Scrappy  the chollo </h1>The Digits are {0} </center>".format(x))
 
 