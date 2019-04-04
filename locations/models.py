from django.db import models

# Create your models here.
class Locations(models.Model):
  name = models.CharField(max_length=40)
  latitude = models.FloatField()
  longitude = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

    