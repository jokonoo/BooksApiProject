from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='authors__name' ,lookup_expr='icontains')
    #author = filters.AllValuesMultipleFilter(field_name='authors__name', lookup_expr='icontains')
    published_date = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'published_date']
