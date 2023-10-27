from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='accesses')
    is_valid = models.BooleanField(default=True)