from django import forms
from django.db.models import TextField

class myform(forms.Form):
    name=forms.CharField(max_length=100)
    Email=forms.EmailField()
    Message=forms.CharField(max_length=100)