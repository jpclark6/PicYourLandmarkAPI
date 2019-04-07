from django.urls import path
from .views import AddUsersView

urlpatterns = [
    path('users/', AddUsersView.as_view(), name='add-user')
]