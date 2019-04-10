from django.urls import path
from .views import AddUsersView, AddUsersLandmark, UpdateUser, UpdateUserLandmark

urlpatterns = [
    path('users/<int:user_pk>/landmarks/<int:landmark_pk>/', UpdateUserLandmark.as_view(), name='update-landmark'),
    path('users/<int:pk>/landmarks/', AddUsersLandmark.as_view(), name='add-landmark'),
    path('users/<int:pk>/', UpdateUser.as_view(), name='update-user'),
    path('users/', AddUsersView.as_view(), name='add-user'),
]