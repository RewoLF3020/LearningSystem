from rest_framework import serializers
from study.models import Lesson, LessonViewInfo


class LessonsSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()
        
    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time')