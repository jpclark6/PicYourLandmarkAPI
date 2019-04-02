from django.db import models

# Create your models here.
class Users(models.Model):
  email = models.CharField
  password_hash = models.CharField

  def __str__(self):
    return self.email