from django.forms import ModelForm

from .models import Table, Item, Profile

class TableForm(ModelForm):
    class Meta: 
        model = Table
        fields = ['table_category', 'table_name', 'table_description']

class ItemForm(ModelForm):
    class Meta: 
        model = Item
        fields = ['item_name', 'item_price']

class ProfileForm(ModelForm):
    class Meta: 
        model = Profile
        fields = '__all__'