from .services import LandmarksService
from .models import Locations

class LandmarksFacade:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

  def get_landmarks_list(self):
    landmarks_json = LandmarksService(self.lat, self.lon).get_landmarks()
    for place in landmarks_json["Response"]["View"][0]["Result"]:
      name = place["Place"]["Name"]
      lat = place["Place"]["Locations"][0]["DisplayPosition"]["Latitude"]
      lon = place["Place"]["Locations"][0]["DisplayPosition"]["Longitude"]
      Locations.objects.get_or_create(
        name=name,
        lat=lat,
        lon=lon
      )
    return Locations.objects.all()

