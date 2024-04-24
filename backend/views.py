from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib import messages
from .forms import *

def is_admin(request):
    if request.user.is_superuser:
        return True


def adminDashboard(request):
    if is_admin(request):
        return render(request,'homepage/admin_dashboard.html')
    return redirect('404')


class HandleAccomodation(APIView):
    
    def get(self,request):
        accommodations = Accommodation.objects.all()
        return render(request,"all/accommodation.html",{"accommodations":accommodations})
    
    def post(self,request):        
        destination = request.POST.get('destination')
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        if destination == "" or name == "" or description == "":
            messages.error(request,"All fields marked * are required!")
            return redirect(request.META.get("HTTP_REFERER"))
        
        
        try:
            accomodation_obj = Accommodation.objects.create(
                destination = destination,
                name = name,
                description = description,
                image = image,
            )
            accomodation_obj.save()
            messages.success(request,"Added")
            return redirect('admin-accomodations')
        
        except Exception as e:
            print(e)
            messages.error(request,f"error - {e}")
            return redirect(request.META.get('HTTP_REFERER'))
        

def EditAccomodation(request):
    
    if request.method == "POST":
        if not(is_admin(request)):
            return redirect('404')
        
        id = request.POST.get('accomodation_id')
        accomodation_obj = Accommodation.objects.filter(id = id)
        
        form = AccommodationForm(request.POST,request.FILES,instance=accomodation_obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated")
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            print(form.errors)
            messages.error(request,f"Error - {form.errors}")
            return redirect(request.META.get('HTTP_REFERER')) 
        
    return render(request,"edit/accommodation.html")    


def DeleteAccommodation(request):
    if request.mehtod == "POST":
        if not(is_admin(request)):
            return redirect('404')
        id = request.POST.get(id)
        accomodation_obj = Accommodation.objects.filter(id = id)
        try:
            accomodation_obj.delete()
            messages.success(request,"Deleted")
            return redirect('accomodations')
        except Exception as e:
            print(e)
            messages.error(request,f"error - {e}")
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('404')
            


class HanldeDestination(APIView):
    
    def get(self,request):
        destinations = Destination.objects.all()
        return render(request,"all/destinations.html",{"destinations":destinations})
    
    def post(self,request):
        try:
            destination_obj = Destination.objects.create(    
                name = request.POST.get('name'),
                location = request.POST.get('location'),
                description = request.POST.get('description'),
                image = request.FILES.get('image'),
                price_500 = request.POST.get('price_500'),
                price_1000 = request.POST.get('price_1000'),
                price_1500 = request.POST.get('price_1500'),
                price_2500_plus = request.POST.get('price_2500_plus'),
            )
            messages.success(request,"Added")
            return redirect('destinations')
        except Exception as e:
            print(e)
            messages.error(request,f"error - {e}")
            return redirect(request.META.get('HTTP_REFERER'))
        
        
        
def EditDestinations(request,id):
    destination_obj = Destination.objects.filter(id = id)
    if request.method =="POST":
        if destination_obj is not None:
            form = DestinationForm(request.POST,request.FILES,instance=destination_obj)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated")
                return redirect(request.META.get('HTTP_REFERER'))
            messages.error(request,f"error - {form.errors}")
            return redirect(request.META.get('HTTP_REFERER'))
        messages.error(request,"No Destination exists with this name")
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request,"edit/destination.html",{"destination":destination_obj.first()})



def DeleteDestination(request,id):
    
    if request.method == "POST":
        try:    
            destination_obj = Destination.objects.filter(id  = id)
            destination_obj.delete()
            messages.success(request,"deleted")
            return redirect('destinations')
        except Exception as e:
            print(e)
            messages.error(request,f"error - {e}")
            return redirect(request.META.get("HTTP_REFERER"))
    
    
        
            
            
    