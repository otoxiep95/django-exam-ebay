from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderProduct, ShoppingCart
from .decorators import check_group
# Create your views here.


@login_required
def index(request):
    context = {}
    return render(request, 'eshop/index.html', context)


@login_required
def customerProductDetail(request):

    user = request.user
    shopping_cart = get_object_or_404(
        ShoppingCart, buyer=user, completed=False)

    context = {'shoppingCartID': shopping_cart.id}

    return render(request, 'eshop/customerproductdetail.html', context)


@login_required
def customerShoppingCart(request):
    user = request.user
    shopping_cart = get_object_or_404(
        ShoppingCart, buyer=user, completed=False)

    context = {'shoppingCartID': shopping_cart.id}

    return render(request, 'eshop/shopping-cart.html', context)


@login_required
def checkout(request):
    user = request.user
    shopping_cart = get_object_or_404(
        ShoppingCart, buyer=user, completed=False)

    context = {'shoppingCartID': shopping_cart.id}

    return render(request, 'eshop/checkout.html', context)


#### Seller views ####
@login_required
# @check_group("seller")
def add_product(request):
    context = {}
    return render(request, 'eshop/create-product.html', context)


@login_required
@check_group("seller")
def update_product(request):
    pass


@login_required
@check_group("seller")
def delete_product(request):
    pass
