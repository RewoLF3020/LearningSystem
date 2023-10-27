from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LessonsViewSet


router = SimpleRouter()
router.register('my-lessons', LessonsViewSet, 'my-lessons')


urlpatterns = [
    path('', include(router.urls))
]
