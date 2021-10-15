from rest_framework import serializers
from .models import Book


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'published_date', 'average_rating', 'ratings_count', 'thumbnail']
