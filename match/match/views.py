from django.shortcuts import render, redirect
from .forms import CreateForm, DeleteForm
from django.conf import settings

def home(request):
    return render(request,'match/home.html')

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            province = form.cleaned_data['province']
            date_of_birth = form.cleaned_data['date_of_birth']

            form = CreateForm()
            message = "Testing"
            return render(request,'match/create.html' , {'form': form,'message': message})

    else:
        form = CreateForm()

    return render(request,'match/create.html' , {'form': form})

def delete(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)

        if form.is_valid():
            record_id = form.cleaned_data['record_id']
            
            form = DeleteForm()
            message = "Testing"
            return render(request,'match/delete.html' , {'form': form,'message': message})

    else:
        form = DeleteForm()

    return render(request,'match/delete.html' , {'form': form})

def matches(request):
    return render(request,'match/matches.html')
