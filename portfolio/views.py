from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from newsapi import NewsApiClient
from .forms import NewsFilterForm
import requests
from django.contrib.auth.decorators import login_required

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

def logout_view(request):
    logout(request)
    return redirect('login')

def project(request):
    projects = Projects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Youre logged in')
            return redirect('home')
        else:
            messages.success(request,'invalid creditials')
            return redirect('/login/')
    return render(request,"login.html")

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('/')
    
@login_required    
def home(request):
    posts = Post.objects.all()[:11]

    cats = Category.objects.all()

    note = Note.objects.all()

    dairy = Dairy.objects.all()
    data={
        'posts':posts,
        'cats' : cats,
        'note' :note,
        'dairy' :dairy,
    }
    return render(request,'home.html',data)  

@login_required
def blogs(request):
    return render(request,"blogs.html") 

@login_required
def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request,'blogs.html',{'post':post, 'cats': cats})

@login_required
def category(request, url):
    cate = Category.objects.get(url=url)
    posts = Post.objects.filter(cate=cate)
    return render(request, "category.html", {'cate': cate, 'posts': posts}) 

@login_required
def profile(request):
    cat = Category.objects.count()
    post = Post.objects.count()
    dairy = Dairy.objects.count()
    notes = Note.objects.count()
    contact = Contact.objects.all()
    return render(request,"profile.html",{'cat':cat,'post':post,'dairy':dairy,'notes':notes,'contact':contact})

@login_required
def addcat(request):
    if request.method=='POST':
        title = request.POST['title']
        discription = request.POST['discription']
        image = request.FILES['image']
        url = request.POST['url']
        category = Category(title=title,discription=discription,image=image,url=url)
        category.save()
        messages.success(request,"Added category")
        return redirect('/home/')

    return render(request,"addcat.html")

@login_required
def noteView(request, url):
    note = Note.objects.get(url=url)
    note1 = Note.objects.all()
    return render(request,'note.html',{'note':note, 'note1': note1})

@login_required
def dairyView(request, url):
    dairy = Dairy.objects.get(url=url)
    dairy1 = Dairy.objects.all()
    return render(request, "dairy.html", {'dairy': dairy, 'dairy1': dairy1}) 

@login_required
def news_list(request):
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])
 
    #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)                

    return render(request, 'home.html')