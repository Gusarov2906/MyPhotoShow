from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        #else:
    return render(request, 'landing/login.html', locals())
