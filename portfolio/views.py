from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def contactHandler(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject2 = request.POST.get('subject')
        message1 = request.POST.get('message')
        print(name)
        query = Contact(name=name,email=email,subject=subject2,message=message1)
        query.save()

        subject = 'THANK YOU FOR CONTACTING ME '
        message = f'Hi {name}, Thank you so much for reaching out to me. Your message brightened my day! '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        
        subject1 = 'HELLOW SIR YOU GOT A NEW MAIL'
        message = f'Hi k satyanarayana chary,  Some one contacted you details are:- \n username - {name},\n  email - {email},\n subject - {subject2},\n message - {message1} \n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list1 = ['charysatheesh4@gmail.com', ]
        send_mail( subject1, message, email_from, recipient_list1 )

        messages.success(request,"Thanks for contacting me ,I will look forward to utilize this oppertunity.....")
        return redirect('/contact/')
    
    return render(request, 'contact.html')

def project(request):
    return render(request,'projects.html')
    
