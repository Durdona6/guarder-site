from django.shortcuts import render
from .models import Service
from apps.index.models import Home

def serviceView(request):
    home = Home.objects.first()
    services = Service.objects.all()
    return render(request, 'service.html', context={
        'services': services,
        'homes' : home,
    })
