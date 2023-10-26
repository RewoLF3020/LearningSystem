from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User,
                              related_name='product_created',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    video_link = models.URLField()
    duration = models.PositiveIntegerField(help_text='Duration in seconds')

class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=200)