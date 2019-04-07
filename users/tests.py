from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from locations.models import Locations
from .models import Users
from .serializers import UsersSerializer
import json


class CreateUsersTest(APITestCase):
    client = APIClient()

    def test_create_a_user(self):
        email = 'test1'
        password = 'test2'
        response = self.client.post(
          f'/api/v1/users/?email={email}&password={password}&password_confirmation=test2'
        )
        self.assertEqual(response.data['email'], email)
        self.assertEqual(response.data['password_hash'], password)

class CreateUserLandmarksTest(APITestCase):
    client = APIClient()

    def test_add_locations(self):
        loc_name = 'Capitol'
        loc_lat = 42.5
        loc_lon = 143.4
        url = 'website.com'
    
        location = Locations.objects.create(name=loc_name, lat=loc_lat, lon=loc_lon)
        user = Users.objects.create(email='email', password_hash='hash')
        
        response = self.client.post(
            f'/api/v1/users/{user.id}/landmarks/?url={url}&location={location.id}'
        )
        self.assertEqual(response.data['status'], 'ok')