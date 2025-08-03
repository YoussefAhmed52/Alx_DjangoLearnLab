from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework import generics, viewsets



def book_list(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"Title: {book.title}, Author: {book.author}<br>"
    return HttpResponse(output)

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    Requires token authentication to access.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    
    permission_classes = [IsAuthenticated]
    
