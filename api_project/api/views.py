from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"Title: {book.title}, Author: {book.author}<br>"
    return HttpResponse(output)

from rest_framework.generics import ListAPIView
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer