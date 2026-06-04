from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['category_id', 'created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model."""
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author', 'description', 'price', 'category', 'category_name', 'created_at', 'updated_at']
        read_only_fields = ['book_id', 'created_at', 'updated_at']
