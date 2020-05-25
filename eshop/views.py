from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderProduct, ShoppingCart

# Create your views here.


def index(request):
    context = {}
    return render(request, 'eshop/index.html', context)


def customerProductDetail(request):

    user = request.user
    shopping_cart = get_object_or_404(
        ShoppingCart, buyer=user, completed=False)

    context = {'shoppingCartID': shopping_cart.id}

    return render(request, 'eshop/customerproductdetail.html', context)


def customerShoppingCart(request):
    user = request.user
    shopping_cart = get_object_or_404(
        ShoppingCart, buyer=user, completed=False)

    context = {'shoppingCartID': shopping_cart.id}

    return render(request, 'eshop/shopping-cart.html', context)


def checkout(request):
    user = request.user
    shopping_cart = get_object_or_404(
        ShoppingCart, buyer=user, completed=False)

    context = {'shoppingCartID': shopping_cart.id}

    return render(request, 'eshop/checkout.html', context)


#### Seller views ####

def add_product(request):
    context = {}
    return render(request, 'eshop/create-product.html', context)


def update_product(request):
    pass


def delete_product(request):
    pass
