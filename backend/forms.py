from .models import *
from django import forms

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = "__all__"
        
        
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = "__all__"