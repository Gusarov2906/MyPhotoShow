from django.shortcuts import render

def lenta(request):
    return render(request, 'landing/lenta.html', locals())
    
def profile(request):
    return render(request, 'landing/profile.html', locals())

def description(request):
    return render(request, 'landing/description.html', locals())

def landing(request):
    return render(request, 'landing/lenta.html', locals())