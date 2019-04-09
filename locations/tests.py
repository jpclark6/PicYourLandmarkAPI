from rest_framework.test import APITestCase, APIClient


class LocationsFromLatLonTest(APITestCase):
    client = APIClient()

    def test_get_landmarks_from_lat_lon(self):
        response = self.client.get(
          '/api/v1/locations/?lat=39.719683&lon=-104.898445'
        )
        self.assertEqual(response.data[0]['name'], 'City of Ulaanbaatar Park')
