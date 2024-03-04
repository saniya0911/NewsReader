from django.shortcuts import render
from newsapi import NewsApiClient
api_key = "6dd0e711b21f4af5bcda4c5151a20534"
# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key=api_key)
    top = newsapi.get_top_headlines(sources='bbc-news,the-next-web,the-times-of-india,the-verge')
    my_articles = top['articles']
    news=[]
    desc=[]
    img=[]
    for i in range(len(my_articles)):
        f = my_articles[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist= zip(news,desc,img)

    return render(request, 'index.html' , context ={"mylist":mylist})
