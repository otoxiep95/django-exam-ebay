from django.db import models
from django.contrib.auth.models import User
#from PIL import Image
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.PROTECT)
    available = models.BooleanField(default=True)
   # image = models.ImageField(default='default.jpg',
    # upload_to='product_images')

    def __str__(self):
        return f"{self.title} - {self.seller}"

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class ShoppingCart(models.Model):
    #order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.PROTECT)
    ordered_date = models.DateTimeField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.buyer.username}"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product.title}"
