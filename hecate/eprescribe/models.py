from django.db import models
from accounts.models import Medical
from datetime import datetime

# Create your models here.
class Prescription(models.Model):
    medical=models.ForeignKey(Medical,on_delete=models.CASCADE)
    literacy=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    sex=models.CharField(max_length=10)
    full_name=models.CharField(max_length=200)
    region=models.CharField(max_length=200)
    patient_email_id=models.CharField(max_length=200)
    doctor_name=models.CharField(max_length=200)
    disease_description=models.CharField(max_length=300,default="N/A")
    date=models.DateTimeField(default=datetime.now,blank=True)


class Medicine(models.Model):
    prescription=models.ForeignKey(Prescription,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    frequency=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    food=models.CharField(max_length=200)
