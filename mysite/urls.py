"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from . import views
from polls import views



# urlpatterns = [
#     # path('', views.Index.as_view(), name='index'),
#     path('', views.index, name='index'),
#     path('polls/', include('polls.urls')),
#     path('page2/', views.page2, name='page2'),
#     path('admin/', admin.site.urls),
# ]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    # path('login', views.Login.as_view(), name='login'),
    # path('tables', views.Tables.as_view(), name='tables')
]
=======
 


urlpatterns = [
    path('status/', include('status.urls')),
    path('polls/', include('polls.urls')),
    path('scrap/', include('scrap.urls')),
    path('', admin.site.urls),
    # path('admin/', admin.site.urls),
]
>>>>>>> 6499d6c1a90149bbab070e377593b754a5b470c1
