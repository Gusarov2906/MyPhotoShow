from django.urls import path
from django.conf.urls import url, include
from myapp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    url('profile.html', views.profile, name='landing'),
    url('editing_profile_info.html', views.edit_profile, name='editing_profile'),
    url('contact.html', views.contact, name='contact'),
    url('feed.html', views.feed, name='feed'),
    url('register.html', views.register, name='register'),
    url('main.html', views.main, name='main'),
    url('index.html', views.main, name='main'),
    url('login.html', views.login_req, name='login'),
    url('creating_post.html', views.create_post, name='create_post'),
    url('accounts/', views.auth, name='auth'),
    url('reg/', views.reg, name='reg'),
    url('edit_profile_info/', views.edit_profile_info, name='auth'),
    url('create_post/', views.add_post, name='reg'),
    url('like/', views.like_post, name='like'),
    url('refresh/', views.refresh, name='like'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url('^$', views.main, name='main'),
]
