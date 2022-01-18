from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('index2', views.index2, name='index2'),
    path('more_blogs/', views.more_blogs, name='more_blogs'),
    # path('<question_id>/', views.blog, name='blog'),
    # path('scrap_show', views.scrap_show, name = 'scrap_show'),
    # path('page2/', views.page2, name='page2'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]