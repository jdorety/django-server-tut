from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Ficion)")

    def __str__(self):
        return self.name

class Books(models.Model):
    """Model representing a book (but not a specific copy of a book)"""
    title = models.CharField(max_length=200)

    