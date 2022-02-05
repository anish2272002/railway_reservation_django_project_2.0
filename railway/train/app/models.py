from django.db import models

# Create your models here.

class user(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    dob=models.DateField()
    gender=models.BooleanField()
    verified=models.BooleanField(default=False)