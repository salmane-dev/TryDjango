from bs4.builder import HTMLTreeBuilder
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


def index(request):
    yes = 1
    title_a = []
    url = 'https://graphicmama.com/blog/page/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    while yes < 30:
        url = 'https://graphicmama.com/blog/page/'+str(yes)+'/'
        print(url)
        r = requests.get(url, headers=headers)
        yes = yes+1
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, features="html.parser")
            articles = soup.find_all('li', class_ = 'post')
            for article in articles:
                title = article.find('h5')
                title_a.append(title.find('a').text)
        else:
            return render(request, 'scrap/index.html', context={'articles':title_a})
    return render(request, 'scrap/index.html', context={'articles':title_a})



def login(request):
    return HttpResponse("Hello, Wellkomen zu Login page")

def index2(request):
    return HttpResponse("Hello, Wellkomen zu page II")
