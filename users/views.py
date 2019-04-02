from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer

# Create your views here.
class AddUserView(generics.RetrieveUpdateDestroyAPIView):
  pass