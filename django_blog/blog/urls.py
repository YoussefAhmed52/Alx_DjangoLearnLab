from django.urls import path 
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView , CommentDeleteView , CommentUpdateView , CommentCreateView)

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_list, name='posts'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.register, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("post/<int:pk>/", CommentCreateView.as_view(), name="post_detail"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]

