from rest_framework import serializers
from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class BooksSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='detailed_api_view',
        lookup_field='pk')

    class Meta:
        model = Book
        fields = ['id',
                  'title',
                  'url',
                  'published_date',
                  'average_rating',
                  'ratings_count',
                  'thumbnail',
                  'authors',
                  'categories']
