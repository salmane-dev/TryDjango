from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
import socket   
import datetime
import os
from django.conf import settings
import httpx
import asyncio
from time import sleep
from typing import List
import random
from asgiref.sync import sync_to_async


 
class index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)
  
  
class checker(LoginRequiredMixin, View):
    template = 'checker.html'
    login_url = '/login/'

    def get(self, request):
        go = my_function()
        return render(request, self.template, {"go1":go[0], "go2":go[1] }) 

def http_call_sync(request): 
    go = my_function() 
    return JsonResponse(go,safe=False)
    

 

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

 

def my_function():
   
    #1194
    Port= 80
    pwd = os.path.dirname(__file__)
    file1 = open(pwd + '/ips.txt')
    Lines = file1.readlines()
    thislist = []
    thatlist = []
    mo = {}
    while True:
        counto = 0 
        # try: 
        time = datetime.datetime.now().strftime("%X") 
        pwd = os.path.dirname(__file__)
        file1 = open(pwd + '/ips.txt')
        Lines = file1.readlines() 
        for line in Lines:
            if line != ' ':
                ip = line.split()[0]
                counto += 1 
                remoteServerIP  = socket.gethostbyname(ip.strip())
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0)
                result = sock.connect_ex((remoteServerIP, Port)) 
                thatlist.append(ip.strip())
                if result == 0: 
                    thislist.append(" Port {} is OPEN for {}".format(Port, ip.strip()))
                else :
                    thislist.append(" Port {} is down for {}".format(Port, ip.strip()))
                sock.close()  
                mo[0] = thatlist
                mo[1] = thislist
        return mo
    # except :
        print("Something went wrong")
    return thislist
         
  