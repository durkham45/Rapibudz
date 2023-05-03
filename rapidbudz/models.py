from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    payment_status = models.BooleanField(default=False)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class About(models.Model):
    image = models.ImageField(upload_to='images/')
    about = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Terms(models.Model):
    terms = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Privacy(models.Model):
    privacy = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Refund(models.Model):
    refund = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Shipping(models.Model):
    shipping = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

