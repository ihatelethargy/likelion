"""myblog URL Configuration

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
from django.urls import path
from mbapp.views import *
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main,name="main"),
    path('about_me/',about,name="about"),

    path('blog/', home, name="home"),
    path('blog/new/', new,name="new"),
    path('blog/create/', create, name="create"),
    path('blog/<str:id>/',detail,name="detail"),
    path('blog/edit/<str:id>',edit,name="edit"),
    path('blog/update/<str:id>',update,name="update"),
    path('blog/delete/<str:id>',delete,name="delete"),

    path('portfolio/', portfolio.views.portfolio, name="portfolio"),   
]
