"""MyPhotoShow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from landing import views

urlpatterns = [
    url('profile', views.profile, name='landing'),
    url('contact', views.contact, name='landing'),
    url('feed', views.feed, name='landing'),
    url('description', views.intro, name='landing'),
    url('register', views.register, name='landing'),
    url('main', views.main, name='landing'),
    url('login', views.login, name='landing'),
    url('', views.landing, name='landing'),
]
