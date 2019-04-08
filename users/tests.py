from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from locations.models import Locations
from .models import Users, UserLocations
from .serializers import UsersSerializer
import json


class CreateUsersTest(APITestCase):
    """
    Test that a user can be created
    """
    client = APIClient()

    def test_create_a_user(self):
        email = 'test1'
        username = 'joe'
        password = 'test2'
        response = self.client.post(
            f'/api/v1/users/?email={email}&username={username}&password={password}&password_confirmation=test2'
        )
        self.assertEqual(response.data['email'], email)
        self.assertEqual(response.data['username'], username)


class CreateUserLandmarksTest(APITestCase):
    """
    Test that locations can be added to an existing user
    """
    client = APIClient()

    def test_add_locations(self):
        loc_name = 'Capitol'
        loc_lat = 42.5
        loc_lon = 143.4
        url = 'website.com'
        location = Locations.objects.create(name=loc_name, lat=loc_lat, lon=loc_lon)
        user = Users.objects.create(email='email', username='username', password_hash='hash')
        response = self.client.post(
            f'/api/v1/users/{user.id}/landmarks/?url={url}&location={location.id}'
        )
        self.assertEqual(response.data['username'], 'username')
        self.assertEqual(response.data['user_locations'][0]['name'], 'Capitol')


class GetUserLandmarksTest(APITestCase):
    """
    Test that a user can get their locations
    """
    client = APIClient()

    def test_add_locations(self):
        loc_name = 'Capitol'
        loc_lat = 42.5
        loc_lon = 143.4
        url = 'website.com'
        email = 'email'
        username = 'username'
        password = 'password'

        location = Locations.objects.create(name=loc_name, lat=loc_lat, lon=loc_lon)
        user = Users.objects.create(email=email, username=username, password_hash=password)
        UserLocations.objects.create(users=user, locations=location, photo_url=url)

        response = self.client.get(
            f'/api/v1/users/?username={username}&password={password}', format='json'
        )
        self.assertEqual(response.data['user_locations'][0]['photo_url'], 'website.com')
