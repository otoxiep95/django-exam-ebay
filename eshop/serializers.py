
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
   class Meta:
      fields = ('id', 'title', 'description', 'price', 'seller')
      model = Product