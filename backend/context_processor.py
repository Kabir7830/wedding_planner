from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

def globalModels(request):

    users = User.objects.all()
    destinations = Destination.objects.all()
    accommodations = Accommodation.objects.all()
    menus = Menu.objects.all()
    decoration = Decoration.objects.all()
    entertainment = Entertainment.objects.all()
    extra = Extra.objects.all()
    services = Services.objects.all()
    packages = Package.objects.all()

    context = {
        "users" :users,
        "destinations" : destinations,
        "accommodations" : accommodations,
        "menus" : menus,
        "decoration" : decoration,
        "entertainment" : entertainment,
        "extra" : extra,
        "services":services,
        # "packages":packages,
    }

    return context