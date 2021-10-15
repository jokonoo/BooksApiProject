from django.shortcuts import render
from rest_framework import generics, filters

from .models import Book
from .serializers import BooksSerializer


class BooksView(generics.ListAPIView):
    serializer_class = BooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['authors', 'published_date']

    def get_queryset(self):

        queryset = Book.objects.all()
        authors = self.request.query_params.get('authors')
        if authors is not None:
            queryset = queryset.filter(authors__name__contains=authors)
        return queryset



