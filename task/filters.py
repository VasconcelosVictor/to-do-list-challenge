import django_filters
from django import forms
from .models import *

class TaskFilter(django_filters.FilterSet):
    STATUS_CHOICES = ((True, 'Concluído'),
                      (False, 'Em Andamento'))

    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES, field_name='status', label='Status')
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at', label='Data de criacao')
    class Meta:
        model = Tasks
        fields = ['user', 'created_at', 'description', 'status']  
        

class TimeRecordFilter(django_filters.FilterSet):
    registration_date = django_filters.DateFromToRangeFilter(field_name='registration_date', label='Data de criacao')
    class Meta:
        model = TimeRecord
        fields = ['task', 'registration_date'] 
