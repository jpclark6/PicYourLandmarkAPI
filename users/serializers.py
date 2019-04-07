from rest_framework import serializers
from .models import Users
from locations.serializers import LocationsSerializer

class UsersSerializer(serializers.ModelSerializer):
  locations = LocationsSerializer(many=True, required=False)
  class Meta:
    model = Users
    fields = ("email", "locations")