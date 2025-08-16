from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer serializes all fields and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer includes nested BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nest related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and nested books
