from django.db import models
from locations.models import Locations

# Create your models here.
class Users(models.Model):
  email = models.CharField(max_length=40, unique=True)
  password_hash = models.CharField(max_length=60)
  locations = models.ManyToManyField('Locations')

  def __str__(self):
    return self.email

    