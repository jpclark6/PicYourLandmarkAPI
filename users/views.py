from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from locations.models import Locations
from .models import Users, UserLocations
from .serializers import UsersSerializer
# Create your views here.
class AddUsersView(APIView):
    """
    Add User
    """
    def post(self, request, *args, **kwargs):
        email = request.query_params.get('email') 
        username = request.query_params.get('username') 
        password_hash = request.query_params.get('password') 
        serializer = UsersSerializer(data={'email': email, 'username': username, 'password_hash': password_hash})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = Users.objects.get(username=request.query_params.get('username'))
        user_locations = UserLocations.objects.filter(users_id=user.id)
        return_hash = {'user_id': user.id, 'username': user.username,'user_locations': []}
        for loc in user_locations:
            full_loc = Locations.objects.get(pk=loc.locations_id)
            return_hash['user_locations'].append({
                'name': full_loc.name,
                'description': full_loc.description,
                'lat': full_loc.lat,
                'lon': full_loc.lon,
                'landmark_id': loc.locations_id,
                'photo_url': loc.photo_url,
                })
        return Response(return_hash, status=status.HTTP_200_OK)

class AddUsersLandmark(APIView):
    """
    Add landmark for user
    """
    def post(self, request, *args, **kwargs):
        user_id = kwargs["pk"]
        landmark_id = request.query_params.get('location')
        photo_url = request.query_params.get('url')
        user = Users.objects.get(pk=user_id)
        landmark = Locations.objects.get(pk=landmark_id)
        UserLocations.objects.create(users=user, locations=landmark, photo_url=photo_url)
        user_locations = UserLocations.objects.filter(users_id=user.id)
        return_hash = {'user_id': user.id, 'username': user.username, 'user_locations': []}
        for loc in user_locations:
            full_loc = Locations.objects.get(pk=loc.locations_id)
            return_hash['user_locations'].append({
                'name': full_loc.name,
                'description': full_loc.description,
                'lat': full_loc.lat,
                'lon': full_loc.lon,
                'landmark_id': loc.locations_id,
                'photo_url': loc.photo_url,
                })
        return Response(return_hash, status=status.HTTP_200_OK)