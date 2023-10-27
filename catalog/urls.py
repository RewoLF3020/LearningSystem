from django.urls import path
from .views import ProductStatisticViewSet


urlpatterns = [
    path('products-statistic/', ProductStatisticViewSet.as_view({'get': 'list'}))
]
