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

TAGS = (
    ('miscellaneous', 'Miscellaneous'),
    ('wearables', 'Wearables'),
    ('consumables', 'Consumables'),
    ('homeables', 'Homeables'),
    ('gardenables', 'Gardenables'),
    ('entertainmentables', 'Entertainables'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 100, default='')
    last_name = models.CharField(max_length= 100, default='')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=9)
    birthday = models.DateField()
    about = models.TextField(max_length=1024)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('home')

class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)
    table_description = models.TextField(max_length=1024)
    table_category = models.CharField(
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
        )

    def __str__(self):
        return self.table_name

    def get_absolute_url(self):
        return reverse('tables_detail', kwargs={'pk': self.id})
    
    def get_absolute_url(self):
        return reverse('tables_update', kwargs={'pk': self.id})

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(max_length=100)
    item_description = models.TextField(max_length=1024, default='')
    # item_picture = models.ForeignKey(Photo, on_delete=models.CASCADE)
    category = models.CharField(
        choices=TAGS,
        default=TAGS[0][0]
        )

    def __str__(self):
        return f'{self.item_name}'

    def get_absolute_url(self):
        return reverse('items_detail')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()
    # Shipping Address?


class Review(models.Model):
    item_rating = models.IntegerField(max_length=5)
    item_review = models.TextField(max_length=1024)


class ItemPhoto(models.Model):
    url = models.CharField(max_length=200)    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class TablePhoto(models.Model):
    url = models.CharField(max_length=200)    
    table = models.ForeignKey(Table, on_delete=models.CASCADE)