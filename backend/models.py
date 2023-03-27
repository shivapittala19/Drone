from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class DroneShot(models.Model):
    name = models.CharField(max_length=255)

class Booking(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    drone_shot = models.ForeignKey(DroneShot, on_delete=models.CASCADE)

