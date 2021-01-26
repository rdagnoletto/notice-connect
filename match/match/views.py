from django.shortcuts import render, redirect
#from .forms import ContactForm
from django.conf import settings

def home(request):
    return render(request,'match/home.html')

def create(request):
    return render(request,'match/create.html')

def delete(request):
    return render(request,'match/delete.html')

def matches(request):
    return render(request,'match/matches.html')
