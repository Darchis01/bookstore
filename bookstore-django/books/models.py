from django.db import models

class Category(models.Model):
    """Category model for organizing books by subject."""
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, help_text="Category name (e.g., Fiction, Science)")
    description = models.TextField(blank=True, help_text="Brief description of the category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Category(id={self.category_id}, name='{self.name}')"


class Book(models.Model):
    """Book model representing books in the bookstore."""
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, help_text="Title of the book")
    author = models.CharField(max_length=255, help_text="Author of the book")
    description = models.TextField(blank=True, help_text="Book description or synopsis")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in Naira")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(id={self.book_id}, title='{self.title}', price={self.price})"
