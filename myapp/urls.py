from django.urls import path
from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url('profile.html', views.profile, name='landing'),
    url('contact.html', views.contact, name='landing'),
    url('feed.html', views.feed, name='landing'),
    url('description.html', views.intro, name='landing'),
    url('register.html', views.register, name='landing'),
    url('main.html', views.main, name='landing'),
    url('login.html', views.loginReq, name='landing'),
    #url('', views.landing, name='landing'),
    url('accountss/', views.auth, name='auth'),
]
