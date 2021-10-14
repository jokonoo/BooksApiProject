from django.db import models


class Books(models.Model):

    title = models.CharField()
    authors = models.CharField()
    published_date = models.CharField()
    categories = models.CharField()
    average_rating = models.IntegerField()
    ratings_count = models.IntegerField()
    thumbnail = models.URLField()
