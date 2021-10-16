from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters

from .models import Book
from .serializers import BooksSerializer
from .filters import BookFilter


class BooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = BookFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if sorting := self.request.query_params.get('sort'):
            queryset = queryset.order_by(sorting)
        return queryset



    #def get_queryset(self):
    #    queryset = Book.objects.all()
    #    #authors = self.request.query_params.get('authors')
    #    if params := self.request.query_params:
    #        queryset = []
    #        print(params)
    #        for v in params.keys():
    #            print(v)
    #            #if v == 'id':
    #            #    queryset.append(Book.objects.filter(id=params.get(v)))
    #            #    print(queryset)
    #            if v == 'published_date':
    #                queryset.append(Book.objects.filter(published_date=params.get(v)))
    #            elif v == 'author' or v == 'authors':
    #                queryset.append(Book.objects.filter(authors__name__contains=params.get(v)))
    #    return queryset


class DetailedBookView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BooksSerializer
