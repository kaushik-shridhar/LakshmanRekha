from django.db import models

# Create your models here.

class Users(models.Model):
    uid = models.CharField(max_length=200)
    patient_name = models.CharField(max_length=200)
    floor_name = models.CharField(max_length=200)
    wifi_ssid = models.CharField(max_length=200)

class Tracker(models.Model):
    uid = models.CharField(max_length=200)
    ssid = models.CharField(max_length=200)
    rssi = models.CharField(max_length=200)
    floor_name = models.CharField(max_length=200)
    mp = models.CharField(max_length=200)

class Wifi(models.Model):
    ssid = models.CharField(max_length=200)
    mp = models.CharField(max_length=200)
    floor_name = models.CharField(max_length=200)
    x = models.CharField(max_length=200)
    y = models.CharField(max_length=200)