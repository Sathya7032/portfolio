from django.urls import path
from .views import index, contactHandler, project


urlpatterns = [
    path('',index,name='index'),
    path('contact/',contactHandler,name='contactHandler'),
    path('projects/',project, name='project')
]
