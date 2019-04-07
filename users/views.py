from django.shortcuts import render
from rest_framework.views import APIView
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
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