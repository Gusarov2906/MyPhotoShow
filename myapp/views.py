from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Person, Post
import os

def feed(request):
    return render(request, 'feed.html', locals())


def profile(request):
    person = Person.objects.filter(id=request.user.id)
    #person.avatar = "../../static/img/profile/1.jpg"
    # posts = Post.objects.all()
    if person.count()>0:
        return render(request, 'profile.html', {'user': request.user, 'person': person[0]})
    else:
        return render(request, 'profile.html', {'user': request.user})


def contact(request):
    return render(request, 'contact.html', locals())


def intro(request):
    return render(request, 'index.html', locals())


def landing(request):
    return render(request, 'index.html', locals())


def main(request):
    count_posts = Post.objects.all().count()
    count_users = User.objects.all().count()
    count_comments = 0
    return render(request, 'main.html', {'count_posts': count_posts, 'count_users': count_users,
                                         'count_comments': count_comments})


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
                person = Person.objects.create(id=user, avatar="../../static/img/profile/1.jpg", description="test")
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

        return HttpResponseRedirect('/profile.html', {'user': request.user})

    return HttpResponseRedirect('/profile.html', {'user': request.user})