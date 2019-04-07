import requests

class LandmarksService:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_landmarks(self):
        url = 'https://geocoder.api.here.com/6.2/search.json' 
        params = {
            'app_id': 'OOmcFqk9piHFxjRmhdlt',
            'app_code': 'BTHUDd_8gGQmen-0dw0isg',
            'mode': 'retrieveLandmarks',
            'prox': f'{self.lat},{self.lon},1000',
            }
        response = requests.get(url, params=params)
        landmarks = response.json()
        return landmarks