from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=500)
    
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=RichTextField()
