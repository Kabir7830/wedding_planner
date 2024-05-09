from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from backend .models import *
from django.db.models import Q
from django.core.paginator import Paginator

User = get_user_model()


def homepage(request):
    special_products = Products.objects.filter(is_published = True).order_by('-id')[:8]
    services = Services.objects.filter(is_published = True)
    return render(request,"homepage/index.html",{"special_products":special_products,"services":services})


def getProductUser(request):
    pass


def about_us(request):
    return render(request,"about/about.html")


def checkout(request):
    return render(request,"checkout/checkout.html")


def cart(request):
    return render(request,"cart/cart.html")

def shop(request):
    items_per_page = 6

    q = request.GET.get('q')
    products = Products.objects.all()
    page_number = request.GET.get('page')
    if q:
        products = Products.objects.filter(Q(tags__icontains = q) | Q(category__name__icontains = q) | Q(price__contains = q))
    paginator = Paginator(products, items_per_page)
    page_obj = paginator.get_page(page_number)
    return render(request,"shop/shop.html",{"products":page_obj,"q":q,"page_number":page_number,"paginator":paginator})

def AllServices(request):
    q = request.GET.get('q')
    services = Services.objects.all()
    if q:
        services = Services.objects.filter(Q(name__icontains = q) | Q(provider_company__icontains = q))
    return render(request,"services/all_services.html",{"services":services,"q":q})

def single_service(request,slug):
    service = Services.objects.filter(slug = slug).first()
    return render(request,"services/service-single.html",{"service":service})



class LoginHandler(APIView):
    
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('homepage')
        return render(request,"authentication/login.html")
    
    def post(self,request):
        if request.user.is_authenticated:
            return Response({"message":"Already Logged In. Redirecting in 2s","status":"success"})
        data = request.data
        print(data)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return Response({"message":"Redirecting in 2s","status":"success"})
        return Response({"message":"Invalid Email or Password","status":"error"})


class RegisterUser(APIView):
    
    def get(self,request):
        
        return render(request,"authentication/signup.html")
    
    def post(self,request):
        
        data = request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        print(first_name)
        if first_name == "" or last_name =="" or email == "" or password == "" or confirm_password == "":
            return Response({"message":"All fields marked with '*' are required!","status":"error"})
        if password != confirm_password:
            return Response({"message":"Passwords do not match!","status":"error"})
        
        existing_obj = User.objects.filter(email = email).first()
        if existing_obj:
            return Response({"message":"Email already taken!","status":"error"})
        try:
            user = User.objects.create_user(
                email = email,
                first_name = first_name,
                last_name = last_name
            )
            
            user.set_password(password)
            user.save()
            return Response({"message":"Account Created. Redirecting to Login page in 2s.","status":"success"})
        except Exception as e:
            print(e)
            return Response({"message":"Server error! Try again in some time.","status":"error"})
        
        

def logoutHandler(request):
    
    if request.user.is_authenticated:
        logout(request)
        return redirect(request.META.get("HTTP_REFERER"))


def register(request):
    return render(request,"authentication/signup.html")


def forgotPassword(request):
    return render(request,"authentication/forgot.html")


def singleProduct(request,slug):
    product = Products.objects.filter(slug = slug).first()
    return render(request,"shop/shop-single.html",{"product":product})


def wishlist(request):
    return render(request,"wishlist/wishlist.html")


class HandleContactForm(APIView):

    def get(self,request):

        return render(request,"contact/contact.html")
    
    def post(self,request):
        try:

            data = request.data
            print(data)
            name = data.get('name')
            email = data.get('email')
            address = data.get('address')
            service = data.get('service')
            message = data.get('message')
            number_of_guests = data.get('number_of_guests')
            meal_preferences = data.get('meal_preferences')
            print(name,email,address,service,message)
            if name == "" or email == "" or address == "" or service == "":
                return Response({"message":"You must fill all the fields!","status":"error"})
            contact_form = Contact.objects.create(
                name = name,
                email = email,
                address = address,
                service = service,
                message = message,
                number_of_guests = number_of_guests,
                meal_preferences = meal_preferences,
                
            )
            print("contactform =", contact_form)
            contact_form.save()
            return Response({"message":"Thankyou for contacting us. You will hear from us soon","status":"success"})
        except Exception as e:
            print(e)
            return Response({"message":"Network Error! Try again in some time.","status":"error"})
        

def contact(request):
    return render(request,"contact/contact.html")


def blogs(request):
    return render(request,"blogs/blogs.html")


def singleBlog(request):
    return render(request,"blogs/blog-single.html")


def error404(request):
    return render(request,"error/404.html")


def AllPackages(request):
    
    return render(request,"packages/all_packages.html")