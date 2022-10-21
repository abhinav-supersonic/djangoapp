from email import message
from django.db import models

# Create your models here.
class contact(models.Model):
    name =models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    number=models.CharField(max_length=10)
    message=models.TextField()