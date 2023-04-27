from django.db import models
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

# class User(models.Model):
    # username = models.CharField(max_length=30)
    # password = models.CharField()
    # seller = models.BooleanField(default=False)
    # email = models.EmailField()
    # address = models.CharField(max_length=100)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # zip = models.IntegerField(max_length=9)
    # birthday = models.DateField()
    # about = models.TextField(max_length=1024)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=9)
    birthday = models.DateField()
    about = models.TextField(max_length=1024)


class Categories(models.Model):
    Categories = models.CharField(
    max_length=1,
    choices=CATEGORIES,
    default=CATEGORIES[0][0]
    )


class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)
    table_description = models.TextField(max_length=1024)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(max_length=100)
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

