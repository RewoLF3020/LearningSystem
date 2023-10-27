from django.contrib import admin
from .models import Lesson, LessonViewInfo


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(LessonViewInfo)
class LessonViewInfo(admin.ModelAdmin):
    pass