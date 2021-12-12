from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context ={
        'variable':'this is sent'
    }
    return render(request, 'index.html',context)
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Form Save successfully!!')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")
