from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

def __str__(self):
    return self.username

class ApplicationForm(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(max_length=8)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    phone=models.TextField()
    email=models.EmailField()
    address=models.TextField()
    district=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    account= models.CharField(max_length=100)
    materials=models.CharField(max_length=100)