from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from locations.models import Locations
from .models import Users
from .serializers import UsersSerializer
# Create your views here.
class AddUsersView(APIView):
    """
    Add User
    """
    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        email = request.query_params.get('email') 
        password_hash = request.query_params.get('password') 
        serializer = UsersSerializer(data={'email': email, 'password_hash': password_hash})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddUsersLandmark(APIView):
    """
    Add landmark for user
    """
    def post(self, request, *args, **kwargs):
        user_id = kwargs["pk"]
        landmark_id = request.query_params.get('landmark')
        photo_url = request.query_params.get('photo_url')
        user = Users.objects.get(pk=user_id)
        landmark = Locations.objects.get(pk=landmark_id)