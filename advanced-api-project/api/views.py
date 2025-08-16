from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

from django_filters.rest_framework import DjangoFilterBackend


# BookListView with filtering, searching, and ordering capabilities
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Allow filtering by these fields
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Allow searching by title and author name
    search_fields = ['title', 'author__name']
    
    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

# Retrieve a single book by ID — allows unauthenticated read
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

# Create a new book — only for authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# Update an existing book — only for authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# Delete a book — only for authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required
