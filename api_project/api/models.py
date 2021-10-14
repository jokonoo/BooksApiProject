from django.db import models


class Books(models.Model):
    id = models.CharField(primary_key=True, max_length=256)
    title = models.CharField(max_length=256)
    published_date = models.CharField(max_length=128)
    average_rating = models.IntegerField()
    ratings_count = models.IntegerField()
    thumbnail = models.URLField()


class Categories(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    books = models.ManyToManyField(Books)


class Authors(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    books = models.ManyToManyField(Books)
