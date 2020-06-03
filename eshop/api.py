from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product, OrderProduct, ShoppingCart
from .serializers import ProductSerializer, OrderProductSerializer, ShoppingCartSerializer
from .permissions import IsOwnerOrNoAccess, IsCustomerOwnerOrNoAccess, IsOwnerOfShoppingCartOrNoAccess


class ProductList(generics.ListCreateAPIView):
    #queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        user_id = self.request.query_params.get(
            'user_id', None)
        if user_id is not None:
            queryset = queryset.filter(seller=user_id)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOfShoppingCartOrNoAccess]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductListInCart(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderProductSerializer

    def get_queryset(self):
        queryset = OrderProduct.objects.all()
        shopping_cart_id = self.request.query_params.get(
            'shopping_cart_id', None)
        if shopping_cart_id is not None:
            queryset = queryset.filter(shopping_cart=shopping_cart_id)
        return queryset


class ShoppingCartList(generics.ListCreateAPIView):

    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        queryset = ShoppingCart.objects.all()
        user_id = self.request.query_params.get(
            'user_id', None)

        if user_id is not None:
            queryset = queryset.filter(buyer=user_id, completed=True)
        return queryset


class ShoppingCartDetail(generics.UpdateAPIView):
    permission_classes = [IsCustomerOwnerOrNoAccess]
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()
