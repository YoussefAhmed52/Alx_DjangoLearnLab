from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_list, name='posts'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]

