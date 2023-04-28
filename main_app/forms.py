from django.forms import ModelForm

from .models import Table, Item

class TableForm(ModelForm):
    class Meta: 
        model = Table
        fields = ['categories', 'table_name', 'table_description']



class ItemForm(ModelForm):
    class Meta: 
        model = Item
        fields = ['categories', 'item_name', 'item_price']