
from rest_framework import serializers
from .models import Product, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'price', 'seller')
        model = Product


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'product', 'shopping_cart')
        model = OrderProduct
