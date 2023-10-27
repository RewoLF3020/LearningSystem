from django.contrib import admin
from .models import Product, ProductAccess


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAccess)
class ProductAccess(admin.ModelAdmin):
    pass