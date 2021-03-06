from django.urls import path,include
from . import views
from .views import home,send_push
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin  
from django.views import defaults 



urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    #path('index2', views.index2, name='index2'),
    path('more_blogs/', views.more_blogs, name='more_blogs'),
    path('home/', views.home, name='home'),
    path('blog/<question_id>/', views.blog, name='blog'),
    path('send_push', views.send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='scrap/sw.js', content_type='application/x-javascript')),
    path("admin/", admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
#handler404 = views.page_not_found_view
#handler404 = 'views.handler404'
#handler500 = 'scrap.views.handler500'

handler404 = 'scrap.views.handler404' #new  

defaults.page_not_found = views.handler404


 