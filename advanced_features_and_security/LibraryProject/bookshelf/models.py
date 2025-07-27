from django.db import models
from django.contrib.auth.models import AbstractUser 
from LibraryProject.relationship_app.models import CustomUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
# Create your models here.
