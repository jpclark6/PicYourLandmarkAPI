from django.urls import path
from .views import AddUsersView, AddUsersLandmark

urlpatterns = [
    path('users/<int:pk>/landmarks/', AddUsersLandmark.as_view(), name='add-landmark'),
    path('users/', AddUsersView.as_view(), name='add-user')
]