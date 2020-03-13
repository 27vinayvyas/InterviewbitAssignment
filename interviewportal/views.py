from django.shortcuts import render
from .models import Participant,Interview
from .forms import UserForm
import sqlite3

# Create your views here.

def home(request):
    #part = Participant.objects.all()
    form=UserForm(request.POST)
    flag=0
    if form.is_valid():
        interviews=Interview.objects.all()
        
        for intervu in interviews:
            if intervu.participant != form.cleaned_data['participant']:
                continue
            if(form.cleaned_data['date_Start']>=form.cleaned_data['date_End']):
                flag=2
                break

            if((form.cleaned_data['date_Start']>=intervu.date_Start and form.cleaned_data['date_Start']<=intervu.date_End)
            or (form.cleaned_data['date_End']>=intervu.date_Start and form.cleaned_data['date_End']<=intervu.date_End)
            or (form.cleaned_data['date_Start']<=intervu.date_Start and form.cleaned_data['date_End']>=intervu.date_End)):
                flag=1
                break
            
        if flag==0:
            form.save()
    
    return render(request,'home.html',{'form':form, 'flag':flag})

def upcoming(request):
    interviews=Interview.objects.all()

    return render(request,'upcoming.html',{'interviews':interviews})

def editing(request,id):
    interview = Interview.objects.filter(count=id).first()
    form = UserForm(request.POST,instance=interview)
    flag=0
    if form.is_valid():
        interviews=Interview.objects.all()
        
        for intervu in interviews:
            if(form.cleaned_data['date_Start']>=form.cleaned_data['date_End']):
                flag=2
                break
            if((form.cleaned_data['date_Start']>=intervu.date_Start and form.cleaned_data['date_Start']<=intervu.date_End)
            or (form.cleaned_data['date_End']>=intervu.date_Start and form.cleaned_data['date_End']<=intervu.date_End)
            or (form.cleaned_data['date_Start']<=intervu.date_Start and form.cleaned_data['date_End']>=intervu.date_End)):
                flag=1
                break
            
        if flag==0:
            form.save()
    
    return render(request,'home.html',{'form':form})


"""
    #interview=Interview.objects.get(count=id)
    form=UserForm(request.POST)

    if form.is_valid:
        #interview=form.save()
        #interview.save()
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = Update Interview set participant=form.participant, date_Start=form.date_start, date_End=form.date_End  where count = id
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    return render(request,'home.html',{'form':form})

"""