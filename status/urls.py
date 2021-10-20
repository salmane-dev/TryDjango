from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index.as_view(), name='index'),
    path('login', views.Login.as_view(), name='login'),
]