from django.urls import path
from . import views
from status.views import async_view, sync_view, smoke_some_meats,burn_some_meats,async_with_sync_view
from django.contrib import admin 

urlpatterns = [ 
    path('', views.index.as_view(), name='index'),
    path('index2', views.index2.as_view(), name='index2'),
    path('login', views.Login.as_view(), name='login'),
    path("admin/", admin.site.urls),
    path("async/",  async_view),
    path("sync/",  sync_view),
    path("smoke_some_meats/", smoke_some_meats),
    path("burn_some_meats/", burn_some_meats),
    path("async_with_sync_view/", async_with_sync_view),
]