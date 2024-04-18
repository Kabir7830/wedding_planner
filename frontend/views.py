from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request,"homepage/index.html")


def about_us(request):
    return render(request,"about/about.html")


def checkout(request):
    return render(request,"checkout/checkout.html")


def cart(request):
    return render(request,"cart/cart.html")

def shop(request):
    return render(request,"shop/shop.html")


def single_service(request):
    return render(request,"services/service-single.html")


def loginHandler(request):
    return render(request,"authentication/login.html")


def register(request):
    return render(request,"authentication/signup.html")


def forgotPassword(request):
    return render(request,"authentication/forgot.html")


def singleProduct(request):
    return render(request,"shop/shop-single.html")


def wishlist(request):
    return render(request,"wishlist/wishlist.html")


def contact(request):
    return render(request,"contact/contact.html")


def blogs(request):
    return render(request,"blogs/blogs.html")


def singleBlog(request):
    return render(request,"blogs/blog-single.html")


def error404(request):
    return render(request,"error/404.html")