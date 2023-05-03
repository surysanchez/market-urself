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
    ('entertainables', 'Entertainables'),
)

TAGS = (
    ('miscellaneous', 'Miscellaneous'),
    ('wearables', 'Wearables'),
    ('consumables', 'Consumables'),
    ('homeables', 'Homeables'),
    ('gardenables', 'Gardenables'),
    ('entertainables', 'Entertainables'),
)
RATING_CHOICES = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
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
    image = models.FileField(upload_to='table_images/', blank=True)

    def __str__(self):
        return self.table_name

    def get_absolute_url(self):
        return reverse('tables_detail', kwargs={'pk': self.id})
    
    def get_absolute_url(self):
        return reverse('tables_update', kwargs={'pk': self.id})

class Item(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(max_length=100)
    item_description = models.TextField(max_length=1024, default='')
    category = models.CharField(
        choices=TAGS,
        default=TAGS[0][0]
        )
    image = models.FileField(upload_to='item_images/', blank=True)

    def __str__(self):
        return f'{self.item_name}'

    def get_absolute_url(self):
        return reverse('items_detail', kwargs={'pk': self.id})

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default='')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(max_length=5, default=1)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)
    item_rating = models.CharField(
        max_length=1,
        choices=RATING_CHOICES, 
        default=RATING_CHOICES[0][0])
    comment = models.TextField(max_length=4000)

    def __str__(self):
        return f'{self.user}'

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()