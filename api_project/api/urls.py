from django.urls import path , include
from .views import book_list , BookList , BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', book_list),
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]