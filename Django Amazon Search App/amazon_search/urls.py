
from django.urls import path
from .views import search_keyword
urlpatterns = [
    path('', search_keyword, name='search_keyword'),
]

