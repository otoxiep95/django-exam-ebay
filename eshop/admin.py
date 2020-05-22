from django.contrib import admin
from .models import Product, OrderProduct, ShoppingCart
# Register your models here.

admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(ShoppingCart)