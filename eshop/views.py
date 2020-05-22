from django.shortcuts import render

# Create your views here.

def index(request):
    context={ }
    return render(request, 'eshop/index.html', context)
    

def add_product(request):
    pass

def update_product(request):
    pass

def delete_product(request):
    pass