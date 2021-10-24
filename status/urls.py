from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index.as_view(), name='index'),
    path('index2', views.index2.as_view(), name='index2'),
    path('login', views.Login.as_view(), name='login'),
]