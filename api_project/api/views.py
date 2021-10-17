from rest_framework import generics
from django_filters import rest_framework as filters
from django.db.models import Q

from .models import Book
from .serializers import BooksSerializer
from .filters import BookFilter


class BooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_class = BookFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        if authors := params.getlist('author'):
            if len(authors) >= 2:
                q = Q()
                for author in authors:
                    q |= Q(authors__name__icontains=author)
                queryset = queryset.filter(q)
                if sorting := params.get('sort'):
                    return queryset.order_by(sorting)
            else:
                queryset = queryset.filter(authors__name__icontains=authors[0])
        if sorting := params.get('sort'):
            queryset = queryset.order_by(sorting)
        return queryset


class DetailedBookView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BooksSerializer
