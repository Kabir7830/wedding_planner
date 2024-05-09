from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

def globalModels(request):

    users = User.objects.all()
    destinations = Destination.objects.all()
    accommodations = Accommodation.objects.all()
    entertainments = Entertainment.objects.all()
    menus = Menu.objects.all()
    decoration = Decoration.objects.all()
    entertainment = Entertainment.objects.all()
    extra = Extra.objects.all()
    services = Services.objects.all()
    packages = Package.objects.all()
    cart_item = []
    total_products_in_cart = 0
    total_oproducts_in_cart = 0
    total_packages_in_cart = 0
    total_price = 0
    orders = Orders.objects.all()
    products = Products.objects.all()
    if request.user.is_authenticated:
        cart_item = Cart.objects.filter(user_id = request.user.id)

        if cart_item.first() is not None:
            for product in cart_item.first().products.all():
                total_price += int(product.price) 
                total_products_in_cart+=1
                total_oproducts_in_cart+=1

            for package in cart_item.first().packages.all():
                total_price+= int(package.total_price)
                total_products_in_cart+=1
                total_packages_in_cart+=1
    if total_oproducts_in_cart == 0 and total_packages_in_cart == 0:
        cart_item = []

    context = {
        "users" :users,
        "destinations" : destinations,
        "accommodations" : accommodations,
        "menus" : menus,
        "decorations" : decoration,
        "entertainment" : entertainment,
        "extra" : extra,
        "services":services,
        "cart_items":cart_item,
        "total_price":total_price,
        "total_products_in_cart":total_products_in_cart,
        "total_oproducts_in_cart":total_oproducts_in_cart,
        "total_packages_in_cart":total_packages_in_cart,
        "orders":orders,
        "products":products,
        "packages":packages,
        "entertainments":entertainments,
        # "packages":packages,
    }

    return context