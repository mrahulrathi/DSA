from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Creates views here.
def index(request):
    # return HttpResponse('this is home page')
    context = {
        'variable' : 'This is sent'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        phone = request.POST.get("phone")
        contact = Contact(name=name, email= email, desc= desc, phone=phone, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, 'contact.html')
