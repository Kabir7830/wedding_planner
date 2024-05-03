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
        
    
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = "__all__"
        

class DiningForm(forms.ModelForm):
    class Meta:
        model = Dining
        fields = "__all__"
        
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        
        
class DecorationForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = "__all__"
        

class EntertainmentForm(forms.ModelForm):
    class Meta:
        model = Entertainment
        fields = "__all__"
        

class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = "__all__"
        
        
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"
        
        
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = "__all__"
        
class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = "__all__"
        
        
class CustomPackageForm(forms.ModelForm):
    class Meta:
        model = CustomPackage
        fields = "__all__"