from django.shortcuts import render


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


def login(request):
    return render(request, 'landing/login.html', locals())
