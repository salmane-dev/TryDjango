from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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
  
  
class index2(LoginRequiredMixin, View):
    template = 'index2.html'
    login_url = '/login/'

    def get(self, request):
        go = my_function()
        return render(request, self.template, {"go1":go[0], "go2":go[1] }) #
 

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
         


#l7ama9


async def http_call_async():
    for num in range(1, 3):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_call_sync():
    for num in range(1, 3):
        sleep(1)
        print(num)
    r = httpx.get("http://httpbin.org/")
    print(r)


# views
 

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")




async def smoke(smokables: List[str] = None, flavor: str = "Sweet Baby Ray's") -> List[str]:
    """ Smokes some meats and applies the Sweet Baby Ray's """

    for smokable in smokables:
        print(f"Smoking some {smokable}...")
        print(f"Applying the {flavor}...")
        print(f"{smokable.capitalize()} smoked.")

    return len(smokables)


async def get_smokables():
    print("Getting smokeables...")

    await asyncio.sleep(2)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

        print("Returning smokeable")
        return [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]


async def get_flavor():
    print("Getting flavor...")

    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

        print("Returning flavor")
        return random.choice(
            [
                "Sweet Baby Ray's",
                "Stubb's Original",
                "Famous Dave's",
            ]
        )


async def smoke_some_meats(request):
    results = await asyncio.gather(*[get_smokables(), get_flavor()])
    total = await asyncio.gather(*[smoke(results[0], results[1])])
    return HttpResponse(f"Smoked {total[0]} meats with {results[1]}!")


### Burnt Meats ###

def oversmoke() -> None:
    """ If it's not dry, it must be uncooked """
    sleep(5)
    print("Who doesn't love burnt meats?")


async def burn_some_meats(request):
    oversmoke()
    return HttpResponse(f"Burned some meats.")


###   Sync to Async   ###


async def async_with_sync_view(request):
    loop = asyncio.get_event_loop()
    async_function = sync_to_async(http_call_sync)
    loop.create_task(async_function())
    return HttpResponse("Non-blocking HTTP request (via sync_to_async)")
















