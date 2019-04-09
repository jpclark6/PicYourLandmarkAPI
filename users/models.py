from django.db import models
from locations.models import Locations


class Users(models.Model):
    """
    Basic user model
    """
    email = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=40, unique=True)
    password_hash = models.CharField(max_length=60)
    profile_url = models.CharField(max_length=120, default='')
    locations = models.ManyToManyField(Locations, through='UserLocations', blank=True)

    def __str__(self):
        return self.username


class UserLocations(models.Model):
    """
    Joins table for users and their locations
    """
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=120)

    def __str__(self):
        return '%s %s' % (self.locations, self.photo_url)
