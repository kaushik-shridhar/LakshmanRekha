from django.db import models

# Create your models here.

# model for storing indoor maps
class Map(models.Model):
    name = models.CharField(max_length=50)
    upload_locn = models.ImageField(upload_to='maps/')
    user = models.CharField(max_length=50)
    geofence_locn = models.ImageField(upload_to='geofenced_maps/')
    coordinates = models.CharField(default="0", max_length=6382)