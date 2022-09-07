from select import select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class CreatePost(forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model = Post
        fields = ['author', 'question', 'content', 'file']
        widgets = {
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'question' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.TextInput(attrs={'class': 'form-control'}),
            'file' : forms.FileInput(attrs={'class' : 'custom-file-input'}),
        }