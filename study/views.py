from django.db.models import Q, FilteredRelation, F
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from catalog.models import ProductAccess
from study.models import Lesson
from .serializers import LessonsSerializer


class LessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = LessonsSerializer 
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        accesses = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        
        qs = Lesson.objects.filter(
            product=accesses.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time')
        )
        
        return qs