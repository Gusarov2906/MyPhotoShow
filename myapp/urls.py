from django.urls import path
from django.conf.urls import url, include
from myapp import views

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
