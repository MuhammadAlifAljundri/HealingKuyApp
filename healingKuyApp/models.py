from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    name_bus= models.CharField(max_length=255)
    depart = models.CharField(max_length=400)
    destination = models.CharField(max_length=400)
    schedule_trip = models.DateTimeField()
    fare = models.FloatField()
    status = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

class Bus(models.Model):
    bus_id= models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    bus_name = models.CharField(max_length=255)
    seats = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=400)   
    status = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    bus_name = models.CharField(max_length=255)
    bus_categoty = models.CharField(max_length=100)
    schedule_trip = models.DateTimeField()
    seats = models.IntegerField()
    payable = models.FloatField()
     
