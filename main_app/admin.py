from django.contrib import admin

from .models import Table, Item, Profile, Review, Cart, CartItem


class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'table_description')

# Register your models here.
admin.site.register(Table)
admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)

