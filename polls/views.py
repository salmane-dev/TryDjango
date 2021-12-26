from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")



class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class Tables(View):
    template = 'tables.html'

    def get(self, request):
        return render(request, self.template)

class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)



def page2(request):
    return HttpResponse("Hello, Wellkomen zu page II")
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)