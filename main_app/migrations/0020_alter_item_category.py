# Generated by Django 4.2 on 2023-05-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_remove_cart_cartitem_cartitem_cart_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('miscellaneous', 'Miscellaneous'), ('wearables', 'Wearables'), ('consumables', 'Consumables'), ('homeables', 'Homeables'), ('gardenables', 'Gardenables'), ('entertainables', 'Entertainables')], default='miscellaneous'),
        ),
    ]
