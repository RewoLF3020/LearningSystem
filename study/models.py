import datetime
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Lesson(models.Model):
    title = models.CharField(max_length=64)
    video_url = models.URLField()
    video_duration = models.PositiveIntegerField(default=0)
    products = models.ManyToManyField(Product)


class LessonStatusEnum(models.TextChoices):
    VIEWED = 'VIEWED'
    NOT_VIEWED = 'NOT_VIEWED'


class LessonViewInfo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=LessonStatusEnum.choices,
                              default=LessonStatusEnum.NOT_VIEWED,
                              max_length=32)
    view_time = models.PositiveIntegerField(default=0)
    last_view_datetime = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        unique_together = ('lesson', 'user')