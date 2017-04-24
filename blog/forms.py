from django import forms
from .models import *

class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=200)