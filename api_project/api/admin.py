from django.contrib import admin
from .models import Book, Category, Author

admin.site.register(Category)
admin.site.register(Author)


@admin.register(Book)
class BookList(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date', 'average_rating', 'ratings_count', 'thumbnail')
# Register your models here.
