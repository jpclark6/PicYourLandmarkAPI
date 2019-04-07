from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Users
from .serializers import UsersSerializer
import json


class LocationsFromLatLonTest(APITestCase):
    client = APIClient()

    def test_create_a_user(self):
        email = 'test1'
        password = 'test2'
        response = self.client.post(
          f'/api/v1/users/?email={email}&password={password}&password_confirmation=test2'
        )
        self.assertEqual(response.data['email'], email)
        self.assertEqual(response.data['password_hash'], password)
