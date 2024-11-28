from django.shortcuts import render
from .models import Guarder
from apps.index.models import Home

def guarView(request):
    home = Home.objects.first()
    guard = Guarder.objects.all()
    return render(request, 'guard.html', context={
        'guards' : guard,
        'homes': home,
    })
