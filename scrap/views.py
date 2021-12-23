from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup




def index(request):
    x = []  
    for i in range(10):
        x.append(i)

    url = 'https://graphicmama.com/blog/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features="html.parser")
    
    articles = soup.find_all('li', class_ = 'post')

    for article in articles:
        title = article.find('h5')
        title_a = title.find('a').text
        print(title_a)
        print('\n')
    print(len(title_a))

    return HttpResponse("<center><h1>Scrappy  the chollo </h1>The Digits are {0} </center>".format(title_a))
 
 