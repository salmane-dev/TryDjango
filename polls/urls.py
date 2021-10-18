from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('login', views.Login.as_view(), name='login'),
    path('page2/', views.page2, name='page2'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



# login page  // https://mkdev.me/en/posts/fundamentals-of-front-end-django