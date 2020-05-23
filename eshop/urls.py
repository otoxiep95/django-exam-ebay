from django.urls import path, include
from . import views
from .api import ProductList, ProductDetail, OrderProductListInCart, OrderProductDetail

app_name = 'eshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail', views.customerProductDetail,
         name="customer_product_detail"),
    path('add_product/', views.add_product, name='add_product'),
    path('shopping_cart/', views.customerShoppingCart, name='shopping_cart'),
    path('update_product/', views.update_product, name='update_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('api/v1/', ProductList.as_view()),
    path('api/v1/<int:pk>/', ProductDetail.as_view()),
    path('api/v1/order_product/', OrderProductListInCart.as_view()),
    path('api/v1/order_product/<int:pk>/', OrderProductDetail.as_view()),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
]
