from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from jiniapis.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):    
    serializer_class = UserSerializer
    queryset = User.objects.all()