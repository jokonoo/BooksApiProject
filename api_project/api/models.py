from django.db import models


class Book(models.Model):
    id = models.CharField(verbose_name="unique id", primary_key=True, max_length=256)
    title = models.CharField(max_length=256)
    published_date = models.CharField(max_length=128, blank=True, null=True)
    average_rating = models.IntegerField(blank=True, null=True, default=None)
    ratings_count = models.IntegerField(blank=True, null=True, default=None)
    thumbnail = models.URLField(verbose_name="thumbnail url", null=True, blank=True, default=None)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    books = models.ManyToManyField(Book, verbose_name="Books list", related_name='categories')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.name
