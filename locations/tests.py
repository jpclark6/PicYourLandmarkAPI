from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Locations
from .serializers import LocationsSerializer
import json


class LocationsFromLatLonTest(APITestCase):
  client = APIClient()

  def test_get_landmarks_from_lat_lon(self):
    response = self.client.get(
      '/api/v1/locations/?lat=39.719683&lon=-104.898445'
    )

    self.assertEqual(1, 1)
