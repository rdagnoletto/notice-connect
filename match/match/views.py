from django.shortcuts import render, redirect
from .forms import CreateForm, DeleteForm
from .models import Record, Match, Notice
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

            r = Record(first_name=first_name, last_name=last_name,province=province,date_of_birth=date_of_birth)
            r.save()
            # Make match entries
            
            form = CreateForm()
            message = "Record Created Successfully"
            return render(request,'match/create.html' , {'form': form,'message': message})
        
        else:
            form = CreateForm()
            message = "Record Creation Failed"
            return render(request,'match/create.html' , {'form': form,'message': message})

    else:
        form = CreateForm()

    return render(request,'match/create.html' , {'form': form})

def delete(request):
    records = Record.objects.all()

    if request.method == 'POST':
        form = DeleteForm(request.POST)

        if form.is_valid():
            record_id = form.cleaned_data['record_id']
            record = Record.objects.filter(pk=record_id)
            if not record:
                message = "Record %d does not exist." % record_id
            else:
                record.delete()
                message = "Success. Record %d has been deleted." % record_id
            form = DeleteForm()

            return render(request,'match/delete.html' , {'form': form,'message': message,'records': records})

    else:
        form = DeleteForm()

    return render(request,'match/delete.html' , {'form': form,'records': records})

def matches(request):
    matches = Match.objects.all()
    return render(request,'match/matches.html', {'matches': matches})
