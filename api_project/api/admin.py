from django.contrib import admin
from .models import Book, Category, Author


@admin.register(Book)
class BookList(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date', 'average_rating', 'ratings_count', 'thumbnail')


@admin.register(Author)
class AuthorList(admin.ModelAdmin):
    fields = ('name', 'books')


@admin.register(Category)
class CategoryList(admin.ModelAdmin):
    fields = ('name', 'books')
