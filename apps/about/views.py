from django.shortcuts import render
from .models import About
from apps.index.models import Home

def aboutView(request):
    home = Home.objects.first()
    about = About.objects.all()
    return render(request, 'about.html', context={
        'abouts' : about,
        'homes' : home,
    })
