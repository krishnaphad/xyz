from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=100)
    city = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=True)
    