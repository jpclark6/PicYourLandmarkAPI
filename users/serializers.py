from rest_framework import serializers
from locations.models import Locations
from locations.serializers import LocationsSerializer
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    """
    This is a serializer for user
    """
    locations = LocationsSerializer(many=True, required=False)
    class Meta:
        model = Users
        fields = ("id", "email", "username", "profile_url", "locations")


class UserLocationsSerializer:
    """
    Custom user serializer
    """
    def __init__(self, user, user_locations):
        self.user = user
        self.user_locations = user_locations

    def data(self):
        """
        Build json to return that includes all user locations with location data
        """
        return_hash = {'user_id': self.user.id, 'username': self.user.username, 'profile_url': self.user.profile_url, 'user_locations': []}
        for loc in self.user_locations:
            full_loc = Locations.objects.get(pk=loc.locations_id)
            return_hash['user_locations'].append({
                'id': loc.id,
                'name': full_loc.name,
                'description': full_loc.description,
                'lat': full_loc.lat,
                'lon': full_loc.lon,
                'landmark_id': loc.locations_id,
                'photo_url': loc.photo_url,
                })
        return return_hash