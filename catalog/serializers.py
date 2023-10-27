from rest_framework import serializers
from .models import Product


class ProductStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    lesson_view_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_users_on_product = serializers.IntegerField()
    purchase_percent = serializers.FloatField()