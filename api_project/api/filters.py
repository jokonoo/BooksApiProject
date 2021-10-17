from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    published_date = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['published_date']
