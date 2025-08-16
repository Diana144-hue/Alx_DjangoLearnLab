from django.db import models

# Create your models here.
from datetime import datetime

# Author model to store writer information
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name

# Book model with a foreign key relationship to Author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # One-to-many relationship

    def __str__(self):
        return self.title
