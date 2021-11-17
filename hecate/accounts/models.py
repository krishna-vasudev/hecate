from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medical(models.Model):
    medical = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

class Patient(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200)
