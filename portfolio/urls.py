from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('contact/',contactHandler,name='contactHandler'),
    path('projects/',project, name='project'),
    path('login/',login_user,name='login_user'),
    path('home/logout/', logout_user, name='logout_user'),
    path('home/',home, name='home'),
    path('home/blog/',blogs, name='blog'),
    path('blog/<slug:url>', post),
    path('home/category/<slug:url>',category),
    path('home/profile/',profile,name='profile'),
    path('home/addcat/',addcat,name='addcat'),
    path('home/addpost/',addpost,name='addpost'),
    path('note/<slug:url>',noteView),
    path('dairy/<slug:url>',dairyView),
]
