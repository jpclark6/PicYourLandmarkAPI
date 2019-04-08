from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from locations.models import Locations
from .models import Users, UserLocations
from .serializers import UsersSerializer, UserLocationsSerializer
# Create your views here.
class AddUsersView(APIView):
    """
    Add User
    """
    def post(self, request, *args, **kwargs):
        email = request.query_params.get('email') 
        password_hash = request.query_params.get('password') 
        serializer = UsersSerializer(data={'email': email, 'password_hash': password_hash})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = Users.objects.get(email=request.query_params.get('email'))
        user_locations = UserLocations.objects.filter(users_id=user.id)
        return_hash = {'user_locations': []}
        for loc in user_locations:
            return_hash['user_locations'].append({'user_id': loc.users_id, 'landmark_id': loc.locations_id, 'photo_url': loc.photo_url})
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
        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)