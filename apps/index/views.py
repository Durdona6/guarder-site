from django.shortcuts import render, redirect
from apps.about.models import About
from apps.service.models import Service
from apps.guard.models import Guarder
from apps.contact.models import Contact
from apps.contact.forms import ContactForm
from .models import Client,Home

def indexView(request):
    home = Home.objects.first()
    client = Client.objects.all()
    about = About.objects.all()
    service = Service.objects.all()
    guarder = Guarder.objects.all()
    contacts = Contact.objects.all()
    form = ContactForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():  # Formani tekshirish
            form.save()  # Ma'lumotlarni saqlash
            return redirect('index')  # So'nggi sahifaga qaytish
    return render(request, 'index.html', context={
        'abouts': about,
        'services': service,
        'guards' : guarder,
        'contacts': contacts,
        'forms': form,
        'clients': client,
        'homes' : home,
    })
