from django.contrib import admin
from .models import Table, Item


class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'table_description')

# Register your models here.
admin.site.register(Table)
admin.site.register(Item)
