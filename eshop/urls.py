from django.urls import path, include
from . import views
from js_urls.views import JsUrlsView
from .api import ProductList, ProductDetail, OrderProductListInCart, OrderProductDetail, ShoppingCartList, ShoppingCartDetail
from django.conf.urls import url
app_name = 'eshop'

JS_URLS = (
    'eshop:shopping_cart',
)

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail', views.customerProductDetail,
         name="customer_product_detail"),
    path('add_product/', views.add_product, name='add_product'),
    path('shopping_cart/', views.customerShoppingCart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_product/', views.update_product, name='update_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('api/v1/', ProductList.as_view()),
    path('api/v1/<int:pk>/', ProductDetail.as_view()),
    path('api/v1/order_product/', OrderProductListInCart.as_view()),
    path('api/v1/order_product/<int:pk>/', OrderProductDetail.as_view()),
    path('api/v1/shopping_cart/', ShoppingCartList.as_view()),
    path('api/v1/shopping_cart/<int:pk>/', ShoppingCartDetail.as_view()),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^js-urls/$', JsUrlsView.as_view(), name='js_urls'),

]
