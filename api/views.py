import json
from datetime import datetime
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# Create your views here.


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls ={
        'Drugs' : 'api/drugs/',
        'Drug Types' : 'api/drug-types/',
        'Authentication' : 'api/user-auth/',
    }
    return Response(api_urls)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_categories(request):
    drugs ={
        '1. ' : 'Cannabis',
        '2. ' : 'Inhalants',
        '3. ' : 'Hallucinogens',       
        '4. ' : 'CNS Stimulants',
        '5. ' : 'Narcotic Analgesics',
        '6. ' : 'Dissociative Anesthetics',
        '7. ' : 'Central Nervous System (CNS) Depressants',
    }
    return Response(drugs)