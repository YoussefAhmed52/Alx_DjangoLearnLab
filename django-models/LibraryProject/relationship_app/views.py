from django.shortcuts import render
from .models import Book , Author , Library , Librarian

def list_books(request):
    books = Book.objects.all()  # get all books from database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# Create your views here.
