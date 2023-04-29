from django.contrib import admin
from .models import Table, Item, Profile


class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'table_description')

# Register your models here.
admin.site.register(Table)
admin.site.register(Item)
admin.site.register(Profile)
