from .models import Post
from django import forms


class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','image','content','url','cate')