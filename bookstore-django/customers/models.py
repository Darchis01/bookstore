from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Customer(models.Model):
    """Customer model representing customers in the bookstore."""
    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=255, help_text="Full name of the customer")
    email = models.EmailField(unique=True, help_text="Email address")
    phone = models.CharField(max_length=15, blank=True, null=True, help_text="Contact phone number")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f"{self.name} ({self.email})"

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name='{self.name}', email='{self.email}')"


class Wishlist(models.Model):
    """Wishlist model to track books users want to read."""
    wishlist_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    books = models.ManyToManyField(Book, related_name='wishlists', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return f"Wishlist for {self.user.username}"

    def __repr__(self):
        return f"Wishlist(user={self.user.username}, books_count={self.books.count()})"
