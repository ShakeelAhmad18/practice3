from django.shortcuts import render
from django import forms
# Create your views here.

class homepage(forms.Form):
    Email=forms.EmailField()
    Password=forms.CharField()

def index(request):
    return render(request,"home/index.html",{
        "forms":homepage()
    })

