from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer

# Create your views here.
class AddUsersView(generics.RetrieveUpdateDestroyAPIView):
  pass