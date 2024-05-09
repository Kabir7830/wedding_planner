from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from backend.views import GetUserOrders
urlpatterns = [
    path('',homepage,name="homepage"),
    path('about/',about_us,name="about"),
    path('checkout/',checkout,name="checkout"),
    path('cart/',cart,name="cart"),
    path('shop/',shop,name="shop"),
    path('shop/<slug:slug>/',singleProduct,name="single-product"),
    path('services/',AllServices,name="all-service"),
    path('service/<slug:slug>/',single_service,name="service"),
    path('login/',LoginHandler.as_view(),name="login"),
    path('register/',RegisterUser.as_view(),name="register"),
    path('forgot/',forgotPassword,name="forgot"),
    path('product/',singleProduct,name="product"),
    path('wishlist/',wishlist,name="wishlist"),
    path('contact/',HandleContactForm.as_view(),name="contact"),
    path('blogs/',blogs,name="blogs"),
    path('single-blog/',singleBlog,name="single-blog"),
    path('404/',error404,name="404"),
    path('logout/',logoutHandler,name="logout"),
    path('orders/',GetUserOrders,name="orders"),
    path('packages/',AllPackages,name="packages"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)