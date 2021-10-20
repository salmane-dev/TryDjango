from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

 
class index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)
  

class Login(View):
    template = 'login.html'

    def get(self, request):
        args = {}
        text = "hello world"
        args['mytext'] = text
        form = AuthenticationForm()
        return render(request, self.template, {'form': form,'args': args})


    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        args = {}
        text = "hello world"
        args['mytext'] = text
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form,'args': args})




def page2(request):
    return HttpResponse("Hello, Wellkomen zu page II")

def page3(request):
    return HttpResponse("Hi, Wellkomen zu page III")