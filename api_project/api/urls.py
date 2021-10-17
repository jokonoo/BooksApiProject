from django.urls import path

from .api_loader import api_loading as api
from .views import BooksView, DetailedBookView

urlpatterns = [
    path('db', api, name='test'),
    path('books', BooksView.as_view(), name='api_view'),
    path('books/<pk>/', DetailedBookView.as_view(), name='detailed_api_view')
]
