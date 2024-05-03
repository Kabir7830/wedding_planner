from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib import messages
from .forms import *

def is_admin(request):
    if request.user.is_superuser:
        return True

def is_method_post(request):
    if request.method == "POST":
        return True
    return False


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
    

def AddProductCategory(request):
    if is_admin(request):
        if is_method_post(request):
            try:
                category = ProductCategory.objects.create(
                    name = request.POST.get('category_name'),
                    slug = request.POST.get('slug'),
                )
                category.save()
                messages.success(request,"Added")
                return redirect('admin-all-categories')
            except Exception as e:
                print(e)
                messages.error(request,f"error - {e}")
                return redirect(request.META.get('HTTP_REFERER'))
        return render(request,"add/category.html")
    return redirect('404')

def EditCategory(request,category_id):
    if is_admin(request):
        category = ProductCategory.objects.filter(id = category_id).first()
        if is_method_post(request):
            form = ProductCategoryForm(request.POST,instance=category)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated")
                return redirect(request.META.get('HTTP_REFERER'))
            messages.error(request,f"error - {form.errors}")
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request,"edit/category.html")
    return redirect('404')

def DeleteCategory(request,category_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                category = ProductCategory.objects.filter(id = category_id)
                category.delete()
                messages.success(request,"Item Removed")
                return redirect('admin-all-categories')
            except Exception as e:
                messages.error(request,f"error - {e}")
                return redirect(request.META.get('HTTP_REFERER'))
        return redirect('404')
    return redirect('404')


def GetAllCategories(request):
    if is_admin(request):
        categories = ProductCategory.objects.all()
        return render(request,"all/categories.html",{"categories":categories})
            


def AddProduct(request):
    if request.user.is_superuser:
        categories = ProductCategory.objects.all()
        if request.method == "POST":
        
            try:
                product = Products.objects.create(
                    name = request.POST.get('name'),
                    category_id = request.POST.get('category'),
                    tags = request.POST.get('tags'),
                    price = request.POST.get('price'),
                    compare_at_price = request.POST.get('compare_at_price'),
                    short_description = request.POST.get('short_description'),
                    description = request.POST.get('description'),
                    images = request.FILES.get('images'),
                    is_published = request.POST.get('is_published',True),
                    slug = request.POST.get('slug'),
                )
                product.save()
                messages.success(request,"Added")
                return redirect("admin-all-products")
            except Exception as e:
                print(e)
                messages.error(request,f"error - {e}")
                return redirect(request.META.get("HTTP_REFERER"))
        return render(request,"add/product.html",{"categories":categories})
    return redirect('404')
    
        
def EditProduct(request,product_id):
    if is_admin(request):
        categories = ProductCategory.objects.all()
        product = Products.objects.filter(id = product_id).first()
        if is_method_post(request):
            if product is not None:
                form = ProductsForm(request.POST,request.FILES,instance=product)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Updated")
                    return redirect(request.META.get('HTTP_REFERER'))
                print(form.errors)
                messages.error(request,f"error - {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
            print("no product found")
            messages.error(request,"No such product exists")
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request,"edit/product.html",{"product":product,"categories":categories})
    return redirect('404')


def DeleteProduct(request,product_id):
    if is_admin(request):
        if is_method_post(request):
            product = Products.objects.filter(id = product_id)
            product.delete()
            messages.success(request,"Item Removed")
            return redirect('admin-all-products')
        return redirect('404')
    return redirect('404')


def GetAllProductsAdmin(request):
    if is_admin(request):
        products = Products.objects.all()
        return render(request,"all/products.html",{"products":products})
    
            
                
def AddService(request):
    
    if is_admin(request):
        if is_method_post(request):
            form = ServiceForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Added")
                return redirect('admin-all-services')
            messages.error(request,f"error - {form.errors}")
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request,"add/service.html")
    return redirect('404')


def EditService(request,service_id):
    if is_admin(request):
        service = Services.objects.filter(id = service_id).first()
        form = ServiceForm()
        if is_method_post(request):
            form = ServiceForm(request.POST,request.FILES,instance=service)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated")
                return redirect(request.META.get('HTTP_REFERER'))
            messages.error(request,f"error - {form.errors}")
            
        return render(request,"edit/service.html",{"service":service})
    return redirect('404')



def DeleteService(request,service_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                service  = Services.objects.filter(id = service_id).first()
                service.delete()
                messages.success(request,"Item Removed")
                return redirect('admin-all-services')
            except Exception as e:
                print(e)
                messages.error(request,f"error - {e}")
                return redirect(request.META.get('HTTP_REFERER'))
        return redirect('404')
    return redirect('404')
    
    
def GetAllServicesAdmin(request):
    if is_admin(request):
        
        services = Services.objects.all()
        return render(request,"all/services.html",{"services":services})
    return redirect('404')


def AddAccommodation(request):
    if is_admin(request):
        destinations = Destination.objects.all()
        if is_method_post(request):
            form = AccommodationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Accommodation added successfully.")
                return redirect('admin-all-accommodations')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = AccommodationForm()
            return render(request, "add/accommodation.html", {"form": form,"destinations":destinations})
    else:
        return redirect('404')

def EditAccommodation(request, accommodation_id):
    if is_admin(request):
        destinations = Destination.objects.all()
        accommodation = Accommodation.objects.filter(id=accommodation_id).first()
        if accommodation:
            if is_method_post(request):
                form = AccommodationForm(request.POST, request.FILES, instance=accommodation)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Accommodation updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = AccommodationForm(instance=accommodation)
            return render(request, "edit/accommodation.html", {"form": form, "accommodation": accommodation,"destinations":destinations})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteAccommodation(request, accommodation_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                accommodation = Accommodation.objects.filter(id=accommodation_id).first()
                if accommodation:
                    accommodation.delete()
                    messages.success(request, "Accommodation deleted successfully.")
                else:
                    messages.error(request, "Accommodation does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-accommodations')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllAccommodationsAdmin(request):
    if is_admin(request):
        accommodations = Accommodation.objects.all()
        return render(request, "all/accommodations.html", {"accommodations": accommodations})
    else:
        return redirect('404')
    
    
def AddDining(request):
    if is_admin(request):
        if is_method_post(request):
            form = DiningForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Dining option added successfully.")
                return redirect('admin-all-dining')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = DiningForm()
            return render(request, "add/dining.html", {"form": form})
    else:
        return redirect('404')

def EditDining(request, dining_id):
    if is_admin(request):
        dining = Dining.objects.filter(id=dining_id).first()
        if dining:
            if is_method_post(request):
                form = DiningForm(request.POST, request.FILES, instance=dining)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Dining option updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = DiningForm(instance=dining)
            return render(request, "edit/dining.html", {"form": form, "dining": dining})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteDining(request, dining_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                dining = Dining.objects.filter(id=dining_id).first()
                if dining:
                    dining.delete()
                    messages.success(request, "Dining option deleted successfully.")
                else:
                    messages.error(request, "Dining option does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-dining')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllDiningAdmin(request):
    if is_admin(request):
        dining_options = Dining.objects.all()
        return render(request, "all/dinings.html", {"dining_options": dining_options})
    else:
        return redirect('404')
    
    
def AddMenu(request):
    if is_admin(request):
        if is_method_post(request):
            form = MenuForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Menu item added successfully.")
                return redirect('admin-all-menu')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = MenuForm()
            return render(request, "add/menu.html", {"form": form})
    else:
        return redirect('404')

def EditMenu(request, menu_id):
    if is_admin(request):
        menu = Menu.objects.filter(id=menu_id).first()
        if menu:
            if is_method_post(request):
                form = MenuForm(request.POST, instance=menu)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Menu item updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = MenuForm(instance=menu)
            return render(request, "edit/menu.html", {"form": form, "menu": menu})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteMenu(request, menu_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                menu = Menu.objects.filter(id=menu_id).first()
                if menu:
                    menu.delete()
                    messages.success(request, "Menu item deleted successfully.")
                else:
                    messages.error(request, "Menu item does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-menu')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllMenuAdmin(request):
    if is_admin(request):
        menu_items = Menu.objects.all()
        return render(request, "all/menus.html", {"menu_items": menu_items})
    else:
        return redirect('404')
    

def AddDecoration(request):
    if is_admin(request):
        if is_method_post(request):
            form = DecorationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Decoration item added successfully.")
                return redirect('admin-all-decoration')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = DecorationForm()
            return render(request, "add/decoration.html", {"form": form})
    else:
        return redirect('404')

def EditDecoration(request, decoration_id):
    if is_admin(request):
        decoration = Decoration.objects.filter(id=decoration_id).first()
        if decoration:
            if is_method_post(request):
                form = DecorationForm(request.POST, instance=decoration)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Decoration item updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = DecorationForm(instance=decoration)
            return render(request, "edit/decoration.html", {"form": form, "decoration": decoration})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteDecoration(request, decoration_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                decoration = Decoration.objects.filter(id=decoration_id).first()
                if decoration:
                    decoration.delete()
                    messages.success(request, "Decoration item deleted successfully.")
                else:
                    messages.error(request, "Decoration item does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-decoration')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllDecorationAdmin(request):
    if is_admin(request):
        decoration_items = Decoration.objects.all()
        return render(request, "all/decorations.html", {"decoration_items": decoration_items})
    else:
        return redirect('404')
    
    
def AddEntertainment(request):
    if is_admin(request):
        if is_method_post(request):
            form = EntertainmentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Entertainment option added successfully.")
                return redirect('admin-all-entertainment')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = EntertainmentForm()
            return render(request, "add/entertainment.html", {"form": form})
    else:
        return redirect('404')

def EditEntertainment(request, entertainment_id):
    if is_admin(request):
        entertainment = Entertainment.objects.filter(id=entertainment_id).first()
        if entertainment:
            if is_method_post(request):
                form = EntertainmentForm(request.POST, instance=entertainment)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Entertainment option updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = EntertainmentForm(instance=entertainment)
            return render(request, "edit/entertainment.html", {"form": form, "entertainment": entertainment})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteEntertainment(request, entertainment_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                entertainment = Entertainment.objects.filter(id=entertainment_id).first()
                if entertainment:
                    entertainment.delete()
                    messages.success(request, "Entertainment option deleted successfully.")
                else:
                    messages.error(request, "Entertainment option does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-entertainment')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllEntertainmentAdmin(request):
    if is_admin(request):
        entertainment_options = Entertainment.objects.all()
        return render(request, "all/entertainments.html", {"entertainment_options": entertainment_options})
    else:
        return redirect('404')    
    
    
    
def AddExtra(request):
    if is_admin(request):
        if is_method_post(request):
            form = ExtraForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Extra item added successfully.")
                return redirect('admin-all-extra')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = ExtraForm()
            return render(request, "add/extra.html", {"form": form})
    else:
        return redirect('404')

def EditExtra(request, extra_id):
    if is_admin(request):
        extra = Extra.objects.filter(id=extra_id).first()
        if extra:
            if is_method_post(request):
                form = ExtraForm(request.POST, instance=extra)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Extra item updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = ExtraForm(instance=extra)
            return render(request, "edit/extra.html", {"form": form, "extra": extra})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteExtra(request, extra_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                extra = Extra.objects.filter(id=extra_id).first()
                if extra:
                    extra.delete()
                    messages.success(request, "Extra item deleted successfully.")
                else:
                    messages.error(request, "Extra item does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-extra')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllExtraAdmin(request):
    if is_admin(request):
        extra_items = Extra.objects.all()
        return render(request, "all/extras.html", {"extra_items": extra_items})
    else:
        return redirect('404')
    
    

def AddPackage(request):
    if is_admin(request):
        if is_method_post(request):
            form = PackageForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Package added successfully.")
                return redirect('admin-all-package')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = PackageForm()
            return render(request, "add/package.html", {"form": form})
    else:
        return redirect('404')

def EditPackage(request, package_id):
    if is_admin(request):
        package = Package.objects.filter(id=package_id).first()
        if package:
            if is_method_post(request):
                form = PackageForm(request.POST, instance=package)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Package updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = PackageForm(instance=package)
            return render(request, "edit/package.html", {"form": form, "package": package})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeletePackage(request, package_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                package = Package.objects.filter(id=package_id).first()
                if package:
                    package.delete()
                    messages.success(request, "Package deleted successfully.")
                else:
                    messages.error(request, "Package does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-package')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllPackageAdmin(request):
    if is_admin(request):
        packages = Package.objects.all()
        return render(request, "all/packages.html", {"packages": packages})
    else:
        return redirect('404')
    

def AddBooking(request):
    if is_admin(request):
        if is_method_post(request):
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Booking added successfully.")
                return redirect('admin-all-booking')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = BookingForm()
            return render(request, "add/booking.html", {"form": form})
    else:
        return redirect('404')

def EditBooking(request, booking_id):
    if is_admin(request):
        booking = Booking.objects.filter(id=booking_id).first()
        if booking:
            if is_method_post(request):
                form = BookingForm(request.POST, instance=booking)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Booking updated successfully.")
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = BookingForm(instance=booking)
            return render(request, "edit/booking.html", {"form": form, "booking": booking})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteBooking(request, booking_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                booking = Booking.objects.filter(id=booking_id).first()
                if booking:
                    booking.delete()
                    messages.success(request, "Booking deleted successfully.")
                else:
                    messages.error(request, "Booking does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-booking')
        else:
            return redirect('404')
    else:
        return redirect('404')

def GetAllBookingAdmin(request):
    if is_admin(request):
        bookings = Booking.objects.all()
        return render(request, "all/bookings.html", {"bookings": bookings})
    else:
        return redirect('404')
    
def GetAllDestinationsAdmin(request):
    if is_admin(request):
        destinations = Destination.objects.all()
        return render(request, "all/destinations.html", {"destinations": destinations})
    else:
        return redirect('404')

def AddDestination(request):
    if is_admin(request):
        if is_method_post(request):
            form = DestinationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Destination added successfully.")
                return redirect('admin-all-destinations')
            else:
                messages.error(request, f"Error: {form.errors}")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = DestinationForm()
            return render(request, "add/destination.html", {"form": form})
    else:
        return redirect('404')

def EditDestination(request, destination_id):
    if is_admin(request):
        destination = Destination.objects.filter(id=destination_id).first()
        if destination:
            if is_method_post(request):
                form = DestinationForm(request.POST, request.FILES, instance=destination)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Destination updated successfully.")
                    return redirect('admin-all-destinations')
                else:
                    messages.error(request, f"Error: {form.errors}")
            else:
                form = DestinationForm(instance=destination)
            return render(request, "edit/destination.html", {"form": form, "destination": destination})
        else:
            return redirect('404')
    else:
        return redirect('404')

def DeleteDestination(request, destination_id):
    if is_admin(request):
        if is_method_post(request):
            try:
                destination = Destination.objects.filter(id=destination_id).first()
                if destination:
                    destination.delete()
                    messages.success(request, "Destination deleted successfully.")
                else:
                    messages.error(request, "Destination does not exist.")
            except Exception as e:
                print(e)
                messages.error(request, f"Error: {e}")
            return redirect('admin-all-destinations')
        else:
            return redirect('404')
    else:
        return redirect('404')
    


def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total_price = CartTotal.objects.get(cart=cart).total_price
    return render(request, 'cart/view_cart.html', {'cart': cart, 'items': items, 'total_price': total_price})


def add_to_cart(request, package_id):
    package = Package.objects.get(pk=package_id)
    form = CartItemForm(request.POST or None)
    if form.is_valid():
        quantity = form.cleaned_data.get('quantity')
        cart = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, package=package)
        if not created:
            item.quantity += quantity
            item.save()
        return redirect('view_cart')
    return render(request, 'cart/add_to_cart.html', {'form': form, 'package': package})


def remove_from_cart(request, item_id):
    item = CartItem.objects.get(pk=item_id)
    item.delete()
    return redirect('view_cart')


def create_custom_package(request):
    if request.method == 'POST':
        form = CustomPackageForm(request.POST)
        if form.is_valid():
            custom_package = form.save()
            # Optionally, perform any additional logic here
            return redirect('custom_package_detail', pk=custom_package.pk)
    else:
        form = CustomPackageForm()
    return render(request, 'create_custom_package.html', {'form': form})

def custom_package_detail(request, pk):
    custom_package = CustomPackage.objects.get(pk=pk)
    return render(request, 'custom_package_detail.html', {'custom_package': custom_package})

def edit_custom_package(request, pk):
    custom_package = CustomPackage.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomPackageForm(request.POST, instance=custom_package)
        if form.is_valid():
            custom_package = form.save()
            # Optionally, perform any additional logic here
            return redirect('custom_package_detail', pk=custom_package.pk)
    else:
        form = CustomPackageForm(instance=custom_package)
    return render(request, 'edit_custom_package.html', {'form': form})

def delete_custom_package(request, pk):
    custom_package = CustomPackage.objects.get(pk=pk)
    if request.method == 'POST':
        custom_package.delete()
        return redirect('homepage')  # Redirect to wherever appropriate
    return render(request, 'delete_custom_package.html', {'custom_package': custom_package})