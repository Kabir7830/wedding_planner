from django.urls import path
from .views import *

urlpatterns = [
    path("",adminDashboard,name="admin-homepage"),
    path("dashboard",adminDashboard,name="dashboard"),
    path("accommodation/",HandleAccomodation.as_view(),name="admin-accommodations"),
    path('add-product/',AddProduct,name="admin-add-product"),
    path('edit-product/<int:product_id>/',EditProduct,name="admin-edit-product"),
    path('delete-product/<int:product_id>/',DeleteProduct,name="admin-delete-product"),
    path('all-products/',GetAllProductsAdmin,name="admin-all-products"),
    path('all-categories/',GetAllCategories,name="admin-all-categories"), 
    path('add-category/',AddProductCategory,name="admin-add-category"),
    path('edit-category/<int:category_id>/',EditCategory,name="admin-edit-category"),
    path('delete-category/<int:category_id>/',DeleteCategory,name="admin-delete-category"),
]
