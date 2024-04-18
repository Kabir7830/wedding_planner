from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',homepage,name="homepage"),
    path('about/',about_us,name="about"),
    path('checkout/',checkout,name="checkout"),
    path('cart/',cart,name="cart"),
    path('shop/',shop,name="shop"),
    path('service-single/',single_service,name="single-service"),
    path('login/',loginHandler,name="login"),
    path('register/',register,name="register"),
    path('forgot/',forgotPassword,name="forgot"),
    path('product/',singleProduct,name="product"),
    path('wishlist/',wishlist,name="wishlist"),
    path('contact/',contact,name="contact"),
    path('blogs/',blogs,name="blogs"),
    path('single-blog/',singleBlog,name="single-blog"),
    path('404/',error404,name="404"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)