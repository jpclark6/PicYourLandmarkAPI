from django.urls import path
from .views import LocationsIndexView

urlpatterns = [
  path('locations/', LocationsIndexView.as_view(), name='locations-index')
]