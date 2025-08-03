from django.urls import path
from .views import book_list , BookList

urlpatterns = [
    path('books/', book_list),
    path('books/', BookList.as_view(), name='book-list'),
]