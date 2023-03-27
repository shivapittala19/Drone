from django.contrib import admin

# Register your models here.
from .models import Location,DroneShot,Customer,Booking
admin.site.register(Location)
admin.site.register(DroneShot)
admin.site.register(Booking)
admin.site.register(Customer)
