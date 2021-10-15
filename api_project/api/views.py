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
        #authors = self.request.query_params.get('authors')
        if params := self.request.query_params:
            queryset = []
            print(params)
            for v in params.keys():
                print(v)
                #if v == 'id':
                #    queryset.append(Book.objects.filter(id=params.get(v)))
                #    print(queryset)
                if v == 'published_date':
                    queryset.append(Book.objects.filter(published_date=params.get(v)))
                elif v == 'author' or v == 'authors':
                    queryset.append(Book.objects.filter(authors__name__contains=params.get(v)))
        return queryset


class DetailedBookView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BooksSerializer
