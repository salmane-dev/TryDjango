from html.parser import HTMLParser
from xml.sax.saxutils import prepare_input_source
from bs4.builder import HTMLTreeBuilder
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
import time
import os
import json
import xml.etree.ElementTree as ET

# import progressbar
# pip install progressbar2
  

def index(request):
    print(request.GET.get('title','default'))

    pwd = os.path.dirname(__file__) 
    x_fil = ET.parse(pwd + '/static/file2.xml')
    # update = ET.SubElement(x_fil.getroot(), "channel")
    # update.text = "new_text"
    # update.attrib["value"] = "1"
    # tree = ET.parse(x_fil)

    root = x_fil.getroot()
    print(root[0][0].text)
    go = len(root[0]) 
    print( go )
    for i in {0,go-1}:  
        print(root[0][i].text )
        print(' [i] ')


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
                img = article.find('img', class_ = 'wp-post-image')['data-lazy-src']
                title = article.find('h5')
                my_link = title.find('a').get("href").rsplit('/', 3)[2]
                articles_list.append({'text':title.find('a').text,
                                    'link':title.find('a').get("href"),
                                    'img':img,
                                    'mylink':my_link 
                                    }) 
        else:
            return render(request, 'scrap/index.html', context={'articles':articles_list, 'page':yes-1})
    return render(request, 'scrap/index.html', context={'articles':articles_list, 'page':yes-1})



def more_blogs(request ): 
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
            img = article.find('img', class_ = 'wp-post-image')['data-lazy-src']
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
    url = 'https://graphicmama.com/blog/'+ question_id
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200: 
        soup = BeautifulSoup(r.content, features="html.parser")
        article = soup.find_all('div', class_ = 'content') 
        title = soup.find('h1').text
        article = str(article).replace('[','\n').replace(']','\n')
        return render(request, 'scrap/blog.html',  context={'go':{'article':article , 'title':title}})
    else:
        return render(request, 'scrap/index.html', context={'go':{'article':"No Article Found", 'page':'fff'}})




def login(request):
    return HttpResponse("Hello, Wellkomen zu Login page")


def index2(request):
    return render(request, 'scrap/index2.html', context={'msg':'Page II'})


