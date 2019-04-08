from rest_framework import serializers
from .models import Users, UserLocations
from locations.serializers import LocationsSerializer

class UserLocationsSerializer(serializers.ModelSerializer):
    """
    User Location serializer
    """
    class Meta:
        model = UserLocations
        fields = ("users_id", "locations_id", "photo_url")

        
class UsersSerializer(serializers.ModelSerializer):
    """
    This is a serializer for user
    """
    locations = LocationsSerializer(many=True, required=False)
    class Meta:
        model = Users
        fields = ("id", "email", "username", "locations")
