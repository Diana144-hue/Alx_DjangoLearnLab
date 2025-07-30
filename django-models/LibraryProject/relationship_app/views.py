from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# function-based view
def list_books(request):
    books = Book.objects.all()
    response = "\n".join([f"{book.title} by {book.author}" for book in books])
    return HttpResponse(response, content_type="text/plain")

# class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
