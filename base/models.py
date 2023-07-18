from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    phone_number = models.CharField(max_length=13, blank=False)
    nrc_number = models.CharField(max_length=60, blank=True)
    profile_pic = models.CharField(max_length=200,blank=True)
    
    

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.TextField(max_length=100)
    client_contact = models.TextField(max_length=500)
    client_description = models.TextField(max_length=500)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)