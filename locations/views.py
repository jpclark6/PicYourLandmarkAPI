from rest_framework import generics
from .serializers import LocationsSerializer
from .facades import LandmarksFacade


class LocationsIndexView(generics.ListAPIView):
    """
    Locations Index
    """

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        return LandmarksFacade(lat, lon).get_landmarks_list()

    serializer_class = LocationsSerializer
