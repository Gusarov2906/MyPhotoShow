from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def feed(request):
    return render(request, 'landing/feed.html', locals())


def profile(request):
    return render(request, 'landing/profile_test.html', {'author_name': 'gusarov2906', 'image': 'profile/2.jpg'})


def contact(request):
    return render(request, 'landing/contact.html', locals())


def intro(request):
    return render(request, 'landing/index.html', locals())


def landing(request):
    return render(request, 'landing/index.html', locals())


def main(request):
    return render(request, 'landing/main.html', locals())


def register(request):
    return render(request, 'landing/register.html', locals())


def loginReq(request):
    return render(request, 'landing/login.html', locals())

def auth(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/profile.html")
        else:
            return HttpResponseRedirect("/login.html")


