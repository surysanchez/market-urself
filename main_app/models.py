from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
CATEGORIES = (
  ('miscellaneous', 'Miscellaneous'),
  ('wearables', 'Wearables'),
  ('consumables', 'Consumables'),
  ('homeables', 'Homeables'),
  ('gardenables', 'Gardenables'),
  ('entertainmentables', 'Entertainables'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=9)
    birthday = models.DateField()
    about = models.TextField(max_length=1024)


class Categories(models.Model):
    categories = models.CharField(
    choices=CATEGORIES,
    default=CATEGORIES[0][0]
    )


class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)
    table_description = models.TextField(max_length=1024)
    # table_logo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(max_length=100)
    # item_picture = models.ForeignKey(Photo, on_delete=models.CASCADE)
    # item_category = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()
    # Shipping Address?


class Review(models.Model):
    item_rating = models.IntegerField(max_length=5)
    item_review = models.TextField(max_length=1024)
    pass


class ItemPhoto(models.Model):
    url = models.CharField(max_length=200)    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class TablePhoto(models.Model):
    url = models.CharField(max_length=200)    
    table = models.ForeignKey(Table, on_delete=models.CASCADE)