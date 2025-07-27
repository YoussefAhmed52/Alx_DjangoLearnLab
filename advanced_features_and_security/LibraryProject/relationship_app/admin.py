from django.contrib import admin
# views/admin_view.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def admin_view(request):
    try:
        if request.user.userprofile.role != 'Admin':
            return redirect('login')  # or use a 403 forbidden page
    except UserProfile.DoesNotExist:
        return redirect('login')

    return render(request, 'roles/admin_view.html')



# Register your models here.
