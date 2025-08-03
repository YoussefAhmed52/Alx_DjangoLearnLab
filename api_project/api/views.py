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