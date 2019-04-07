from django.db import models
from locations.models import Locations

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=40, unique=True)
    password_hash = models.CharField(max_length=60)
    locations = models.ManyToManyField(Locations, through='UserLocations', blank=True)

    def __str__(self):
        return self.email

class UserLocations(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=120)

    def __str__(self):
        return '%s %s' % (self.locations, self.photo_url)
