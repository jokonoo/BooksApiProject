import requests

from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Book, Category, Author


@csrf_exempt
def api_loading(request):
    if request.method == "POST":
        url = 'https://www.googleapis.com/books/v1/volumes'
        data = {'q': request.GET.get('q', '')}
        r = requests.get(url, data).json()
        for item in r.get("items"):
            item_data = item.get("volumeInfo")
            obj, created = Book.objects.update_or_create(
                id=item.get("id"), defaults={'id': item.get("id"),
                                             'title': item_data.get("title"),
                                             'published_date': item_data.get("publishedDate"),
                                             'average_rating': item_data.get("averageRating"),
                                             'ratings_count': item_data.get("ratingsCount")})
            if thumbnail := item_data.get("imageLinks"):
                obj.thumbnail = thumbnail.get("thumbnail")
                obj.save()
            if author_list := item.get("volumeInfo").get("authors"):
                for author in author_list:
                    auth, created = Author.objects.get_or_create(name=author)
                    obj.authors.add(auth)
            if category_list := item.get("volumeInfo").get("categories"):
                for category in category_list:
                    cat, created = Category.objects.get_or_create(name=category)
                    obj.categories.add(cat)
    return HttpResponseRedirect(reverse('api_view'))
