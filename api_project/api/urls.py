from django.urls import path
from .api_loader import api_loading as api

urlpatterns = [
    path('<param>/', api, name='test')
]
