from rest_framework import serializers
from .models import Users, UserLocations
from locations.models import Locations
from locations.serializers import LocationsSerializer

# class UserLocationsSerializer(serializers.ModelSerializer):
#     """
#     User Location serializer
#     """
#     class Meta:
#         model = UserLocations
#         fields = ("users_id", "locations_id", "photo_url")

        
class UsersSerializer(serializers.ModelSerializer):
    """
    This is a serializer for user
    """
    locations = LocationsSerializer(many=True, required=False)
    class Meta:
        model = Users
        fields = ("id", "email", "username", "locations")

class UserLocationsSerializer:
    """
    Custom user serializer
    """
    def __init__(self, user, user_locations):
        self.user = user
        self.user_locations = user_locations

    def data(self):
        return_hash = {'user_id': self.user.id, 'username': self.user.username,'user_locations': []}
        for loc in self.user_locations:
            full_loc = Locations.objects.get(pk=loc.locations_id)
            return_hash['user_locations'].append({
                'name': full_loc.name,
                'description': full_loc.description,
                'lat': full_loc.lat,
                'lon': full_loc.lon,
                'landmark_id': loc.locations_id,
                'photo_url': loc.photo_url,
                })
        return return_hash