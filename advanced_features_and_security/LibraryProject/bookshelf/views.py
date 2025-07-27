from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

# Only users with 'can_edit' permission can access this view
@permission_required('library_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    books = get_object_or_404(Book, id=book_id)
    # Logic to edit the book (form, POST/GET handling)
    return render(request, 'edit_book.html', {'book_list': books})\
        
def search_view(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'results': results})
# Create your views here.
