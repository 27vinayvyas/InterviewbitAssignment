from django import forms
from .models import Participant, Interview

part = Participant.objects.all()

Fruit=[]

for i in part:
    Fruit.append(('i',i.name))

class UserForm(forms.ModelForm):
    class  Meta:
        model = Interview
        fields = ['participant','date_Start','date_End']

"""
    participant= forms.CharField(widget=forms.Select(choices=Fruit))
    date_Start = forms.DateTimeField()
    date_End = forms.DateTimeField()
"""