from django.shortcuts import render, redirect
from .models import Library , Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required , login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import UserProfile

def is_admin(user):
   
    if not user.is_authenticated:
        return False
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    
    if not user.is_authenticated:
        return False
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    
    if not user.is_authenticated:
        return False
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'



@login_required
@user_passes_test(is_admin)
def admin_view(request):
   
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    
    return render(request, 'member_view.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('home')  # Replace 'home' with your main page name
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect to role-specific view
            role = user.userprofile.role
            if role == 'Admin':
                return redirect('admin_view')
            elif role == 'Librarian':
                return redirect('librarian_view')
            elif role == 'Member':
                return redirect('member_view')
            else:
                return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def list_books(request):
    books = Book.objects.all()  # get all books from database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
# Create your views here.
