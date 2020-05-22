from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.seller}"

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product.title}"

class ShoppingCart(models.Model):
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.buyer.username}"