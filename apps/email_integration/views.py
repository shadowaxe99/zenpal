
from django.shortcuts import render
from .models import Email

def index(request):
    emails = Email.objects.all()
    return render(request, 'email_integration/index.html', {'emails': emails})

def send_email(request):
    if request.method == 'POST':
        email = Email()
        email.subject = request.POST.get('subject')
        email.message = request.POST.get('message')
        email.to = request.POST.get('to')
        email.save()
        email.send()
        return render(request, 'email_integration/index.html', {'message': 'Email sent successfully'})
    else:
        return render(request, 'email_integration/send_email.html')
