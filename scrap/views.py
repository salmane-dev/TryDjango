from bs4.builder import HTMLTreeBuilder
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import time
# import progressbar
# pip install progressbar2

def index(request):
    yes = 1
    articles_list = []
    url = 'https://graphicmama.com/blog/page/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

    # for i in progressbar.progressbar(range(20)):
    #     time.sleep(0.1)

    while yes < 2:
        url = 'https://graphicmama.com/blog/page/'+str(yes)+'/' 
        r = requests.get(url, headers=headers)
        yes = yes+1
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, features="html.parser")
            articles = soup.find_all('li', class_ = 'post')
            for article in articles:
                img = article.find('img', class_ = 'wp-post-image')['src']
                title = article.find('h5')
                my_link = title.find('a').get("href").rsplit('/', 3)[2]
                articles_list.append({'text':title.find('a').text,
                                    'link':title.find('a').get("href"),
                                    'img':img,
                                    'mylink':my_link    
                                    }) 
        else:
            return render(request, 'scrap/index.html', context={'articles':articles_list})
    return render(request, 'scrap/index.html', context={'articles':articles_list})


def blog(request, question_id):
 
    url = 'https://graphicmama.com/blog/'+ question_id
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        # time.sleep(2)
        print("got get it")
        soup = BeautifulSoup(r.content, features="html.parser")
        article = soup.find_all('div', class_ = 'post__entry') 
        return render(request, 'scrap/blog.html', context={'article':article})
    else:
        return render(request, 'scrap/index.html', context={'article':"article"})






def login(request):
    return HttpResponse("Hello, Wellkomen zu Login page")


def index2(request):
    return render(request, 'scrap/index2.html', context={'msg':'Page II'})


