from django.db import models
from django.contrib.auth.models import User
from product1.models import Product1

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product1, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart Item: {self.product.title}"
