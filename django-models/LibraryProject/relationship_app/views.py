from django.shortcuts import render, redirect
from .models import Library , Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import UserProfile

# Helper decorator to check roles
def role_required(role_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You are not logged in.")
            if not hasattr(request.user, 'userprofile'):
                return HttpResponseForbidden("No profile found.")
            if request.user.userprofile.role != role_name:
                return HttpResponseForbidden(f"You must be a {role_name} to access this page.")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'roles/admin_view.html')


@login_required
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'roles/librarian_view.html')


@login_required
@role_required('Member')
def member_view(request):
    return render(request, 'roles/member_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Register View
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
    


# Create your views here.
