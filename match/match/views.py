from django.shortcuts import render, redirect
from .forms import CreateForm, DeleteForm
from .models import Record, Match, Notice
from django.conf import settings
from django.db.models import Q

def make_matches(record):
    # all weak, possible, and strong matches.
    weak = Notice.objects.filter(Q(first_name=record.first_name)|Q(alt_first_name=record.first_name)).filter(Q(last_name=record.last_name)|Q(alt_last_name=record.last_name))
    # all possible and strong matches.
    possible = weak.filter(province=record.province)
    # all strong matches.
    strong = possible.filter(date_of_birth=record.date_of_birth)

    # all matches minus possible and strong matches equals weak matches only.
    weak = weak.difference(possible)
    # possible and strong matches minus strong matches equal possible matches only.
    possible = possible.difference(strong)

    # add all matches to database with correct code for match type.
    for n in strong:
        match = Match(record=record,notice=n,m_type='S')
        match.save()
    
    for n in possible:
        match = Match(record=record,notice=n,m_type='P')
        match.save()
    
    for n in weak:
        match = Match(record=record,notice=n,m_type='W')
        match.save()

# home page with links to pages for create, delete, and matches.
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
            # valid form, create record and call function to create matches.
            r = Record(first_name=first_name, last_name=last_name,province=province,date_of_birth=date_of_birth)
            r.save()

            make_matches(r)

            # reset form and ready page for another record creation with a message.
            form = CreateForm()
            message = "Record Created Successfully"
            return render(request,'match/create.html' , {'form': form,'message': message})
        
        else:
            # if the form wasn't valid pass back message to user.
            form = CreateForm()
            message = "Record Creation Failed"
            return render(request,'match/create.html' , {'form': form,'message': message})

    else:
        # if not post, just create empty form and return page.
        form = CreateForm()

    return render(request,'match/create.html' , {'form': form})

def delete(request):
    # Query all records to diplay them.
    records = Record.objects.all()

    if request.method == 'POST':
        form = DeleteForm(request.POST)

        if form.is_valid():
            record_id = form.cleaned_data['record_id']
            record = Record.objects.filter(pk=record_id)
            # Check if record exist by pk, if it does delete and return success message, else error message.
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

# Send all matches to template to be displayed.
def matches(request):
    matches = Match.objects.all()
    return render(request,'match/matches.html', {'matches': matches})
