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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
