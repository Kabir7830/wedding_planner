from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser
from django.utils.text import slugify


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Remove the username field

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Add your additional fields here
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Add any other required fields

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Accommodation(models.Model):
  id = models.AutoField(primary_key=True)
  destination = models.ForeignKey('Destination', on_delete=models.CASCADE)  # This should be linked to your destination model
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='accommodations/')
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.name)  # Generate slug from title
      super().save(*args, **kwargs)
      
      

class Dining(models.Model):
  
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='dining/')
  price_less_500 = models.CharField(max_length=100, null=True,blank=True)
  price_500 = models.CharField(max_length=100, null=True,blank=True)
  price_1000 = models.CharField(max_length=100, null=True,blank=True)
  price_1500 = models.CharField(max_length=100, null=True,blank=True)
  price_2000_plus = models.CharField(max_length=100, null=True,blank=True)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
      
      
class Destination(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='destinations/')
  price_500 = models.DecimalField(max_digits=10, decimal_places=2)
  price_1000 = models.DecimalField(max_digits=10, decimal_places=2)
  price_1500 = models.DecimalField(max_digits=10, decimal_places=2)
  price_2500_plus = models.DecimalField(max_digits=10, decimal_places=2)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.name)  # Generate slug from title
      super().save(*args, **kwargs)
      
      
  class Meta:
    db_table = 'destination'

class Menu(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
      
      
  class Meta:
    db_table = 'menu'

class Decoration(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
      
      
  class Meta:
    db_table = 'decoration'

class Entertainment(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
      
      
  class Meta:
    db_table = 'entertainment'

class Extra(models.Model):  # This model represents anything that can be extra
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  type = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
      
  class Meta:
     db_table = "extras"

class Package(models.Model):
   
    class Meta:
      db_table = "package"
    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    accomodation = models.ForeignKey(Accommodation,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    decoration = models.ForeignKey(Decoration,on_delete=models.CASCADE)
    entertainment = models.ForeignKey(Entertainment,on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra,on_delete=models.CASCADE)
    total_price = models.CharField(max_length = 255)

class Booking(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  package = models.ForeignKey(Package,on_delete=models.CASCADE)


class ProductCategory(models.Model):
  class Meta:
      db_table = "product_categories"
    
  name = models.CharField(max_length=255)
  slug = models.SlugField(blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
      
      
class Products(models.Model):
  class Meta:
      db_table = "products"

  name = models.CharField(max_length=255)
  category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
  tags = models.CharField(max_length=255,null=True,blank=True)
  price = models.CharField(max_length=100)
  compare_at_price = models.CharField(max_length=100,null=True,blank=True)
  short_description = models.CharField(max_length=255,null=True,blank=True)
  description = models.TextField()
  images = models.ImageField(upload_to='products/')
  is_published = models.BooleanField(default=True,null=True,blank=True)

  slug = models.SlugField(unique=True,blank=True)  # Ensure unique slugs and allow blank

  def save(self, *args, **kwargs):
      if not self.slug:  # If slug is not set
          self.slug = slugify(self.title)  # Generate slug from title
      super().save(*args, **kwargs)
  

class Content(models.Model):
  class Meta:
     db_table = "contents"

  file = models.FileField(upload_to='contents/files/')
  date_added = models.CharField(max_length=100)


class Services(models.Model):
    class Meta:
        db_table = "services"
        
    name = models.CharField(max_length=255)
    description = models.TextField()
    provider_name = models.CharField(max_length=255)
    provider_company = models.CharField(max_length=255)
    provider_number = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    compare_at_price = models.CharField(max_length=10,null=True,blank=True)
    image = models.ImageField(upload_to='service_img/',null=True,blank=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField('Package', through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.package.name} in {self.cart}"

class CartTotal(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Total price of cart {self.cart}"
    
    
class CustomPackage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    destinations = models.ManyToManyField('Destination')
    menus = models.ManyToManyField('Menu')
    accommodations = models.ManyToManyField('Accommodation')
    decorations = models.ManyToManyField('Decoration')
    entertainments = models.ManyToManyField('Entertainment')
    extras = models.ManyToManyField('Extra')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class Contact(models.Model):
   
  class Meta:
      db_table = "contact"

  name = models.CharField(max_length=255)
  email = models.EmailField()
  address = models.TextField()
  service = models.CharField(max_length=255)
  message = models.TextField(blank=True,null=True)
  number_of_guests = models.CharField(max_length=255,blank=True,null=True)
  meal_preferences = models.CharField(max_length=255,blank=True,null=True)
   



