from django.urls import path
from . import views 
from django.contrib import admin  


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('checker', views.checker.as_view(), name='checker'),
    path('http_call_sync', views.http_call_sync, name='http_call_sync'),
    path('login', views.Login.as_view(), name='login'),
    path("admin/", admin.site.urls) ,
]

