from django.db import models
import datetime 

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class Interview(models.Model):
    count = models.AutoField(primary_key=True)
    participant = models.ForeignKey(Participant, related_name='participants',on_delete=models.PROTECT)
    date_Start = models.DateField(null=True)#( default=datetime.date.today,null=False)
    date_End = models.DateField(null=True) #( default=datetime.date.today,null=False)

    def __str__(self):
        return self.participant.name

