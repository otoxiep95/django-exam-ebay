# Generated by Django 3.0.6 on 2020-06-01 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop', '0005_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eshop.Product'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='shopping_cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eshop.ShoppingCart'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]