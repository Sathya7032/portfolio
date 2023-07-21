from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def contactHandler(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name)
        query = Contact(name=name,email=email,subject=subject,message=message)
        query.save()
        messages.success(request,"Thanks for contacting me ,I will look forward to utilize this oppertunity.....")
        return redirect('/contact/')
    
    return render(request, 'contact.html')

def project(request):
    return render(request,'projects.html')
    
