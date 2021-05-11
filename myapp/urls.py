from django.urls import path
from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url('profile.html', views.profile, name='landing'),
    #url('profile_test.html', views.profile, name='landing'),
    url('contact.html', views.contact, name='contact'),
    url('feed.html', views.feed, name='feed'),
    url('description.html', views.intro, name='description'),
    url('register.html', views.register, name='register'),
    url('main.html', views.main, name='main'),
    url('index.html', views.main, name='index'),
    url('login.html', views.login_req, name='login'),
    url('accounts/', views.auth, name='auth'),
    url('reg/', views.reg, name='reg'),
    #url('', views.landing, name='landing'),
]
