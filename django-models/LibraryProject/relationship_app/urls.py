from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LogoutView , LoginView


urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]