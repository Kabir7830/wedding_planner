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
        

class ProductsForm(forms.ModelForm):
    class Meta:
        
        model = Products
        fields  ="__all__"
        
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"