from django.db import models

class Product1(models.Model):
    image = models.ImageField(upload_to='product1s/')
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
