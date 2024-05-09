from django.urls import path
from .views import *

urlpatterns = [
    path("",adminDashboard,name="admin-homepage"),
    path("dashboard",adminDashboard,name="dashboard"),
    # path("accommodation/",HandleAccomodation.as_view(),name="admin-accommodations"),
    path('all-products/',GetAllProductsAdmin,name="admin-all-products"),
    path('add-product/',AddProduct,name="admin-add-product"),
    path('edit-product/<int:product_id>/',EditProduct,name="admin-edit-product"),
    path('delete-product/<int:product_id>/',DeleteProduct,name="admin-delete-product"),
    
    path('all-categories/',GetAllCategories,name="admin-all-categories"), 
    path('add-category/',AddProductCategory,name="admin-add-category"),
    path('edit-category/<int:category_id>/',EditCategory,name="admin-edit-category"),
    path('delete-category/<int:category_id>/',DeleteCategory,name="admin-delete-category"),
    
    path('all-services/',GetAllServicesAdmin,name="admin-all-services"),
    path('add-service/',AddService,name="admin-add-service"),
    path('edit-service/<int:service_id>/',EditService,name="admin-edit-service"),
    path('delete-service/<int:service_id>/',DeleteService,name="admin-delete-service"),
    
    path("all-accommodations/", GetAllAccommodationsAdmin, name="admin-all-accommodations"),
    path("add-accommodation/", AddAccommodation, name="admin-add-accommodation"),
    path("edit-accommodation/<int:accommodation_id>/", EditAccommodation, name="admin-edit-accommodation"),
    path("delete-accommodation/<int:accommodation_id>/", DeleteAccommodation, name="admin-delete-accommodation"),
    
    path("all-menus/", GetAllMenuAdmin, name="admin-all-menus"),
    path("add-menu/", AddMenu, name="admin-add-menu"),
    path("edit-menu/<int:menu_id>/", EditMenu, name="admin-edit-menu"),
    path("delete-menus/<int:menu_id>/", DeleteMenu, name="admin-delete-menu"),
    
    path("all-decorations/", GetAllDecorationAdmin, name="admin-all-decorations"),
    path("add-decoration/", AddDecoration, name="admin-add-decoration"),
    path("edit-decoration/<int:decoration_id>/", EditDecoration, name="admin-edit-decoration"),
    path("delete-decoration/<int:decoration_id>/", DeleteDecoration, name="admin-delete-decoration"),
    
    path("all-entertainments/", GetAllEntertainmentAdmin, name="admin-all-entertainments"),
    path("add-entertainment/", AddEntertainment, name="admin-add-entertainment"),
    path("edit-entertainment/<int:entertainment_id>/", EditEntertainment, name="admin-edit-entertainment"),
    path("delete-entertainment/<int:entertainment_id>/",DeleteEntertainment , name="admin-delete-entertainment"),
    
    path("all-extras/", GetAllExtraAdmin, name="admin-all-extras"),
    path("add-extra/", AddExtra, name="admin-add-extra"),
    path("edit-extra/<int:extra_id>/", EditExtra, name="admin-edit-extra"),
    path("delete-extra/<int:extra_id>/", DeleteExtra, name="admin-delete-extra"),
    
    path("all-packages/", GetAllPackageAdmin, name="admin-all-packages"),
    path("add-package/", AddPackage, name="admin-add-package"),
    path("edit-package/<int:package_id>/", EditPackage, name="admin-edit-package"),
    path("delete-package/<int:package_id>/", DeletePackage, name="admin-delete-package"),
    
    path("all-bookings/", GetAllBookingAdmin, name="admin-all-bookings"),
    path("add-booking/", AddBooking, name="admin-add-booking"),
    path("edit-booking/<int:booking_id>/", EditBooking, name="admin-edit-booking"),
    path("delete-booking/<int:booking_id>/", DeleteBooking, name="admin-delete-booking"),
    
    path("all-destinations/", GetAllDestinationsAdmin, name="admin-all-destinations"),
    path("add-destination/", AddDestination, name="admin-add-destination"),
    path("edit-destination/<int:destination_id>/", EditDestination, name="admin-edit-destination"),
    path("delete-destination/<int:destination_id>/", DeleteDestination, name="admin-delete-destination"),
    
    path("all-dinings/", GetAllDiningAdmin, name="admin-all-dinings"),
    path("add-dining/", AddDining, name="admin-add-dining"),
    path("edit-dining/<int:dining_id>/", EditDining, name="admin-edit-dining"),
    path("delete-dining/<int:dining_id>/", DeleteDining, name="admin-delete-dining"),

    path('add-to-cart/',add_to_cart,name="add-to-cart"),
    path('add-to-cart-product/<int:product_id>/',Add_To_Cart_Product,name="add-to-cart-product"),
    path('add-to-cart-package/<int:package_id>/',Add_To_Cart_Package,name="add-to-cart-package"),
    path('remove-product-from-cart/<int:product_id>/',Remove_product_Form_cart,name="remove-product-from-cart"),
    path('remove-package-from-cart/<int:package_id>/',Remove_pAckage_From_Cart,name="remove-package-from-cart"),

    path('place-order/',PlaceOrder,name="place-order"),
    path('admin-orders/',AdminGetUserOrders,name="admin-orders"),
    
]
