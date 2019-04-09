from django.urls import path
from .views import AddUsersView, AddUsersLandmark, UpdateUser

urlpatterns = [
    path('users/<int:pk>/landmarks/', AddUsersLandmark.as_view(), name='add-landmark'),
    path('users/<int:pk>/', UpdateUser.as_view(), name='update-user'),
    path('users/', AddUsersView.as_view(), name='add-user'),
]