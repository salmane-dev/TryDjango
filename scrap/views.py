from html.parser import HTMLParser
from xml.sax.saxutils import prepare_input_source
from bs4.builder import HTMLTreeBuilder 
import requests
from bs4 import BeautifulSoup 
import os
import xml.etree.ElementTree as ET
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification 
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings  
from time import sleep
from typing import List 
from asgiref.sync import sync_to_async 
from django.views.decorators.http import require_GET, require_POST
import json 
import pprint 
# from django.shortcuts import render_to_response
# from django.template import RequestContext



# import progressbar
# pip install progressbar2
  

def custom_404(request, exception):
    print("request")
    print(request)
    return render(request, "scrap/404.html")



def custom_404(request, exception):  
    print("request")
    print(request)
    return HttpResponse('<h1>4040404040404<h1>' )

    

  
@require_GET
# @csrf_exempt
def home(request):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    return render(request, 'home.html', {user: user, 'vapid_key': vapid_key})

   
@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)
        print("data")
        print(data)
        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})
        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})



 
def index(request):
    print("index index index index")
    print(request.GET.get('title','default'))
    pwd = os.path.dirname(__file__) 
    x_fil = ET.parse(pwd + '/static/file2.xml')
    # update = ET.SubElement(x_fil.getroot(), "channel")
    # update.text = "new_text"
    # update.attrib["value"] = "1"
    # tree = ET.parse(x_fil)

    root = x_fil.getroot()
    #print(root[0][0].text)
    ji = len(root) 
    go = len(root[0]) 
    # print( root[0] )
    for item in root.iter("item"):
        print(item.text)  
        # item.text = str(new_rank)
        # item.set('changed', 'yes') 
    yes = 1
    articles_list = []
    page = int(request.GET.get('page'))+1 if  request.GET.get('page')  else 1
    url = 'https://graphicmama.com/blog/page/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    while yes <= 1:
        url = 'https://graphicmama.com/blog/page/'+str(yes)+'/' 
        r = requests.get(url, headers=headers)
        yes = yes+1
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, features="html.parser")
            articles = soup.find_all('li', class_ = 'post')
            for article in articles:
                title = article.find('h5')
                img = article.find('img' )['data-lazy-src']
                my_link = title.find('a').get("href").rsplit('/', 3)[2]
                articles_list.append({'text':title.find('a').text,
                                    'link':title.find('a').get("href"),
                                    'img':img,
                                    'mylink':my_link 
                                    })  
        else:
                return HttpResponse('<h1>4040404040404<h1>', status=404)
    return render(request, 'scrap/index.html', context={'articles':articles_list, 'page':yes-1})


def more_blogs(request): 
    print("more_blogs more_blogs more_blogs more_blogs")
    print(request.GET.get('title','default'))
    #sanitazation za3ma
    # try:  
    #     print ("ssssssssssssssssssssssssssssssssss")
    #     print (type(int(request.GET.get('page')))) 
    # except AttributeError: 
    #     print ("except except except except except")
    #     print("not a valid number")
    #     return HttpResponse('Something Definitely Went Wrong')
 
    page = int(request.GET.get('page'))
    articles_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    url = 'https://graphicmama.com/blog/page/'+str(page)+'/' 
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, features="html.parser")
        articles = soup.find_all('li', class_ = 'post')
        for article in articles:
            # img = article.find('img', class_ = 'wp-post-image')['data-lazy-src']
            img = article.find('img' )['data-lazy-src']
            title = article.find('h5')
            my_link = title.find('a').get("href").rsplit('/', 3)[2]
            articles_list.append({'text':title.find('a').text,
                                'link':title.find('a').get("href"),
                                'img':img,
                                'mylink':my_link 
                                }) 
        articles_list.append({'page':page})
    else:
        data = json.dumps( articles_list )
        return JsonResponse(data,safe=False)
    data = json.dumps( articles_list )
    return JsonResponse(data,safe=False)


 
def blog(request, question_id): 
    print("blog blog blog blog blog")
    url = 'https://graphicmama.com/blog/'+ question_id
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    if r.status_code == 200: 
        soup = BeautifulSoup(r.content, features="html.parser")
        article = soup.find_all('div', class_ = 'content') 
        title = soup.find('h1').text
        article = str(article).replace('[','\n').replace(']','\n')
        return render(request, 'scrap/blog.html',  context={'go':{'article':article , 'title':title}})
    else:
        return render(request, 'scrap/index.html', context={'go':{'article':'404', 'page':'0'}})




def index1(request):
    return HttpResponse("Hello, Wellkomen zu Login page")


def index2(request, exception):
    print("request")
    print(exception)
    return HttpResponse('<h1> index2 <h1>' )


