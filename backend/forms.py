from django import forms
from .models import Location,DroneShot,Booking

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'address')
        labels = {
            'name': 'Name',
            'address': 'Address',
        }
        
class DroneForm(forms.ModelForm):
    class Meta:
        model = DroneShot
        fields = ['name']
        labels = {
            'name': 'Name',  
        }




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['drone_shot']

