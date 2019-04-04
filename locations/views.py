from django.shortcuts import render
from rest_framework import generics
from .models import Locations
from .serializers import LocationsSerializer

# Create your views here.
class LocationsIndexView(generics.ListAPIView):
    """
    Locations Index
    """
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
