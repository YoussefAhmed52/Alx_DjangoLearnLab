from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# 1. List all books
class BookListView(generics.ListAPIView):
    class BookListView(generics.ListAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        permission_classes = [permissions.AllowAny]

    # Enable DRF filter backends
        filter_backends = [
        DjangoFilterBackend,  # Filtering
        filters.SearchFilter, # Search
        filters.OrderingFilter # Ordering
    ]

    # 1. Filtering fields (exact matches unless overridden)
        filterset_fields = ['title', 'author', 'published_date']

    # 2. Search fields (partial match, case-insensitive)
        search_fields = ['title', 'author']

    # 3. Ordering fields
        ordering_fields = ['title', 'published_date']
        ordering = ['title']  # Default ordering

# 2. Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read access

# 3. Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# 4. Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# 5. Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 