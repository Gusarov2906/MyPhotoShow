from django.shortcuts import render

def feed(request):
    return render(request, 'landing/feed.html', locals())
    
def profile(request):
    return render(request, 'landing/profile.html', locals())

def contact(request):
    return render(request, 'landing/contact.html', locals())

def intro(request):
    return render(request, 'landing/index.html', locals())

def landing(request):
    return render(request, 'landing/index.html', locals())