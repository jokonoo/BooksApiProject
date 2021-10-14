from django.db import models


class Books(models.Model):
    id = models.CharField(primary_key=True, max_length=256)
    title = models.CharField(max_length=256)
    published_date = models.CharField(max_length=128)
    average_rating = models.IntegerField(blank=True, null=True, default=None)
    ratings_count = models.IntegerField(blank=True, null=True, default=None)
    thumbnail = models.URLField(null=True, blank=True, default=None)


class Categories(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    books = models.ManyToManyField(Books)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    books = models.ManyToManyField(Books)

    def __str__(self):
        return self.name
