from django.forms import ModelForm

from .models import Table, Item

class TableForm(ModelForm):
    class Meta: 
        model = Table
        fields = ['table_category', 'table_name', 'table_description']



class ItemForm(ModelForm):
    class Meta: 
        model = Item
        fields = ['item_name', 'item_price']