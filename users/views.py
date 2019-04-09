from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from locations.models import Locations
from .models import Users, UserLocations
from .serializers import UsersSerializer, UserLocationsSerializer


class AddUsersView(APIView):
    """
    Create user and get info for user
    """
    def post(self, request, *args, **kwargs):
        """
        POST /api/v1/users/
        """
        email = request.query_params.get('email')
        username = request.query_params.get('username')
        password_hash = request.query_params.get('password')
        serializer = UsersSerializer(
            data={'email': email, 'username': username, 'password_hash': password_hash}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """
        GET /api/v1/users/
        """
        try:
            user = Users.objects.get(username=request.query_params.get('username'))
            user_locations = UserLocations.objects.filter(users_id=user.id)
            return_hash = UserLocationsSerializer(user, user_locations).data()
            return Response(return_hash, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class AddUsersLandmark(APIView):
    """
    Add landmark for user
    """
    def post(self, request, *args, **kwargs):
        """
        POST /api/v1/users/:id/landmarks
        """
        try:
            landmark_id = request.query_params.get('location')
            photo_url = request.query_params.get('url')
            user = Users.objects.get(pk=kwargs["pk"])
            landmark = Locations.objects.get(pk=landmark_id)
            UserLocations.objects.create(users=user, locations=landmark, photo_url=photo_url)
            user_locations = UserLocations.objects.filter(users_id=user.id)
            return_hash = UserLocationsSerializer(user, user_locations).data()
            return Response(return_hash, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUser(APIView):
    """
    Add user profile picture
    """
    def patch(self, request, *args, **kwargs):
        """
        PATCH /api/v1/users/:id/
        """
        try:
            profile_url = request.query_params.get('profile_url')
            user = Users.objects.get(pk=kwargs["pk"])
            user.profile_url = profile_url
            user.save()
            serializer = UsersSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)