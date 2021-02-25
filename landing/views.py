from django.shortcuts import render

def lenta(request):
    return render(request, 'landing/lenta.html', locals())
    
def profile(request):
    return render(request, 'landing/tmp/profile.html', locals())

def intro(request):
    return render(request, 'landing/index.html', locals())

def landing(request):
    return render(request, 'landing/index.html', locals())