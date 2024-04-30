from django.forms import ModelForm
from .models import *
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name','author_email','text')
        labels = {
            'author_name': 'Имя',
            'author_email': 'Почта',
            'text': 'Текст',
        }
       

