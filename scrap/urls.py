from django.urls import path,include
from . import views
from .views import home,send_push
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home', home, name='home'),
    path('login', views.login, name='login'),
    path('index2', views.index2, name='index2'),
    path('more_blogs/', views.more_blogs, name='more_blogs'),
    path('<question_id>/', views.blog, name='blog'),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)