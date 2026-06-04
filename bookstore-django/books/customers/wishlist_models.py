from django.db import models
from django.contrib.auth.models import User
from books.models import Book


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
