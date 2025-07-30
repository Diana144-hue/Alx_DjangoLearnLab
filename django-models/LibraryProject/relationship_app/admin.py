from django.contrib import admin

# Register your models here.
from .models import Book, Author, Library, Librarian

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)