from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LogoutView , LoginView


urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
]