from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Person, Post, UsersLikedPosts
import json

import os


def feed(request):
    posts = Post.objects.order_by('date_of_publication')[::-1]
    return render(request, 'feed.html', {'posts': posts})


def profile(request):
    person = Person.objects.filter(id=request.user.id)
    posts = Post.objects.filter(author=person.first())

    if person.count() > 0:
        return render(request, 'profile.html', {'user': request.user, 'person': person[0], 'posts': posts})
    else:
        return render(request, 'profile.html', {'user': request.user})


def contact(request):
    return render(request, 'contact.html', locals())

def main(request):
    count_posts = Post.objects.all().count()
    count_users = User.objects.all().count()
    count_likes = UsersLikedPosts.objects.all().count()
    return render(request, 'main.html', {'count_posts': count_posts, 'count_users': count_users,
                                         'count_likes': count_likes})


def register(request):
    return render(request, 'register.html', locals())


def login_req(request):
    return render(request, 'login.html', locals())


def auth(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect("/profile.html")
            person = Person.objects.filter(id=request.user.id)
            return HttpResponseRedirect('/profile.html', {'user': user, 'person': person})
        else:
            return HttpResponseRedirect("/login.html")


def reg(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        email = request.POST.get('email', False)
        firstname = request.POST.get('name', False)
        lastname = request.POST.get('surname', False)
        birthdate = request.POST.get('birthdate', False)

        # TODO: check if already existed
        if username and password and email and firstname and lastname:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=firstname,
                                            last_name=lastname)
            if Person.objects.filter(id=user.id).count() == 0:
                person = Person.objects.create(id=user, avatar="../../static/img/profile/default.png", description=" ")
                try:
                    os.mkdir("././media/img/profile/" + str(user.id))
                except OSError as error:
                    print(error)
            else:
                person = Person.objects.filter(id=request.user.id)
            login(request, user)
            return HttpResponseRedirect('/profile.html', {'user': user, 'person': person})
        else:
            return HttpResponseRedirect("/register.html")


def create_post(request):
    return render(request, 'creating_post.html', locals())


def edit_profile(request):
    return render(request, 'editing_profile_info.html', locals())


def edit_profile_info(request):
    if request.method == "POST":
        description = request.POST.get('description', False)
        img = request.FILES.get('img', False)
        person = Person.objects.filter(id=request.user.id).first()
        if description:
            person.description = description
        if img:
            person.avatar = img
        person.save()
        return HttpResponseRedirect('/profile.html', {'user': request.user, 'person': person})
    return HttpResponseRedirect('/profile.html', {'user': request.user})


def add_post(request):
    if request.method == "POST":
        img = request.FILES.get('img', False)
        person = Person.objects.filter(id=request.user.id)
        posts = Post.objects.filter(author=person.first())
        posts.create(author=person.first(), img=img, number_of_likes=0)
        return HttpResponseRedirect('/profile.html', {'user': request.user, 'person': person, 'posts': posts})
    return HttpResponseRedirect('/profile.html', {'user': request.user})


def like_post(request):
    #print("hello")
    global ctx
    if request.method == "POST":
        post_id = request.POST.get('post_id', False)
        person = Person.objects.filter(id=request.user.id).first()
        posts = Post.objects.filter(author=person)
        post = Post.objects.filter(id=post_id).first()
        postLikedUser = UsersLikedPosts.objects.filter(person=person, post=post)
        #print(post_id)
        if postLikedUser:
            post.number_of_likes -= 1
            postLikedUser.delete()
        else:
            post.number_of_likes += 1
            UsersLikedPosts.objects.create(person=person, post=post)
        post.save()
        ctx = {'post_id': post.id, 'likes_count': post.number_of_likes}
        #return HttpResponseRedirect('/profile.html', {'user': request.user, 'person': person, 'posts': posts})
    return HttpResponse(json.dumps(ctx))
    #return HttpResponseRedirect('/profile.html', {'user': request.user})

def refresh(request):
  posts = Post.objects.all()
  data = []
  for post in posts:
    data.append({"likes_count": post.number_of_likes, "id": post.id})
  return HttpResponse(json.dumps(data))

