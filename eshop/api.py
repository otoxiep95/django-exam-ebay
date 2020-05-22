from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrNoAccess


class ProductList(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer