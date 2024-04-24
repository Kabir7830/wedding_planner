from django.urls import path
from .views import *

urlpatterns = [
    path("",adminDashboard,name="admin-homepage"),
    path("dashboard",adminDashboard,name="dashboard"),
    path("accommodation/",HandleAccomodation.as_view(),name="admin-accommodations"),
]
