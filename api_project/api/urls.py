from django.urls import path
from .api_loader import api_loading as api, test

urlpatterns = [
    path('<param>/', api, name='test'),
    path('auth/test/', test, name='author_test')
]
