import requests
from .models import Books, Categories, Authors
from django.shortcuts import render


def api_loading(request, param):
    url = 'https://www.googleapis.com/books/v1/volumes'
    data = {'q': param}
    r = requests.get(url, data).json()
    for item in r.get("items"):
        obj, created = Books.objects.update_or_create(
            id=item.get("id"), defaults={'id': item.get("id"),
                                         'title': item.get("volumeInfo").get("title"),
                                         'published_date': item.get("volumeInfo").get("publishedDate"),
                                         'average_rating': item.get("volumeInfo").get("averageRating"),
                                         'ratings_count': item.get("volumeInfo").get("ratingsCount")})
        if thumb := item.get("volumeInfo").get("thumbnail"):
            obj.thumbnail = thumb
        if author_list := item.get("volumeInfo").get("authors"):
            for author in author_list:
                auth, created=Authors.objects.get_or_create(name=author)
                auth.books.add(obj)
        if category_list := item.get("volumeInfo").get("categories"):
            for category in category_list:
                cat, created=Categories.objects.get_or_create(name=category)
                cat.books.add(obj)
    return render(request, 'api/test.html', context={'objects': Books.objects.all()})