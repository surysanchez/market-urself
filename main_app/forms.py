from django.forms import ModelForm

from .models import Table, Item, Profile, Review

class TableForm(ModelForm):
    class Meta: 
        model = Table
        fields = ['table_category', 'table_name', 'table_description', 'image']

class ItemForm(ModelForm):
    class Meta: 
        model = Item
        fields = ['item_name', 'item_price', 'image']

class ProfileForm(ModelForm):
    class Meta: 
        model = Profile
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [ 'item_rating', 'comment']