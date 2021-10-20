from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

 
class index(View):
    template = 'index.html'
    def get(self, request):
        return render(request, self.template)


def page2(request):
    return HttpResponse("Hello, Wellkomen zu page II")

def page3(request):
    return HttpResponse("Hi, Wellkomen zu page III")