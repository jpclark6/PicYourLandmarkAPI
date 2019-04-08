from django.db import models

# Create your models here.
class Locations(models.Model):
    """
    Locations AKA landmarks model
    """
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, null=True, blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name