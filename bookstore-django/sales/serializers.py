from rest_framework import serializers
from .models import Sale
from books.serializers import BookSerializer
from customers.serializers import CustomerSerializer


class SaleSerializer(serializers.ModelSerializer):
    """Serializer for Sale model."""
    book_details = BookSerializer(source='book', read_only=True)
    customer_details = CustomerSerializer(source='customer', read_only=True)

    class Meta:
        model = Sale
        fields = [
            'sale_id', 'customer', 'book', 'date', 'quantity',
            'total_price', 'book_details', 'customer_details', 'created_at', 'updated_at'
        ]
        read_only_fields = ['sale_id', 'date', 'total_price', 'created_at', 'updated_at']


class SaleCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating sales."""

    class Meta:
        model = Sale
        fields = ['book', 'quantity']

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value
