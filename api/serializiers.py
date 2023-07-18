from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Client, Customer


class ClientSerializier(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('client_id', 'client_name', 'client_contact', 'client_description')
        
        
        
#Customers (Users)

class CustomerSerializier(serializers.ModelSerializer):
    firstname = serializers.CharField(source='auth.first_name')
    lastname = serializers.CharField(source='auth.last_name')
    email = serializers.CharField(source='auth.email')
    class Meta:
        model = Customer
        fields = ('customer_id', 'firstname', 'lastname', 'email','phone_number', 'nrc_number', 'profile_pic')