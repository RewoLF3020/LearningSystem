from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LessonsViewSet, LessonsByProductViewSet


router = SimpleRouter()
router.register('my-lessons', LessonsViewSet, 'my-lessons')


urlpatterns = [
    path('by-product/<int:product_id>/lessons', LessonsByProductViewSet.as_view({'get': 'list'})),
    path('', include(router.urls))
]
