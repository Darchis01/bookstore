from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['customer_id', 'user', 'name', 'email', 'phone', 'created_at', 'updated_at']
        read_only_fields = ['customer_id', 'created_at', 'updated_at']


class SignUpSerializer(serializers.Serializer):
    """Serializer for user sign up."""
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('name', '').split()[0] if validated_data.get('name') else '',
            last_name=' '.join(validated_data.get('name', '').split()[1:]) if validated_data.get('name') else '',
        )
        customer = Customer.objects.create(
            user=user,
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data.get('phone', '')
        )
        return customer


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
