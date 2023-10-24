
from django.shortcuts import render
from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_management/index.html', {'contacts': contacts})

def detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact_management/detail.html', {'contact': contact})

def create(request):
    if request.method == 'POST':
        new_contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        new_contact.save()
        return redirect('contact_management:index')
    else:
        return render(request, 'contact_management/create.html')

def update(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.save()
        return redirect('contact_management:detail', contact_id=contact.id)
    else:
        return render(request, 'contact_management/update.html', {'contact': contact})

def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact_management:index')
