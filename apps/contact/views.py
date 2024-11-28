from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from apps.index.models import Home

def contact_view(request):
    home = Home.objects.first()
    contacts = Contact.objects.all()
    form = ContactForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():  # Formani tekshirish
            form.save()  # Ma'lumotlarni saqlash
            return redirect('index')  # So'nggi sahifaga qaytish
    return render(request, 'contact.html', context={
        'contacts': contacts,
        'forms': form,  # Formani konteksta yuborish
        'homes' : home,
    })


