from django.urls import path

from .api_loader import api_loading as api, test
from .views import BooksView

urlpatterns = [
    path('get/<param>/', api, name='test'),
    path('auth/test/', test, name='author_test'),
    path('api/view/', BooksView.as_view(), name='api_view')
]
