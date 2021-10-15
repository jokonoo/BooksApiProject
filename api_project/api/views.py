from django.shortcuts import render
from rest_framework import generics

from .models import Book
from .serializers import BooksSerializer


class BooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer



