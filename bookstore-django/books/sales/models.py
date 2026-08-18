from django.db import models
from django.core.validators import MinValueValidator
from books.customers.models import Customer
from books.models import Book


class Sale(models.Model):
    """Sale model representing transactions in the bookstore."""
    sale_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sales')
    date = models.DateField(auto_now_add=True, help_text="Date of the transaction")
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of copies purchased"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total price for this transaction",
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def save(self, *args, **kwargs):
        """Calculate total price before saving."""
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sale #{self.sale_id} - {self.customer.name} bought {self.book.title}"

    def __repr__(self):
        return f"Sale(id={self.sale_id}, customer={self.customer.name}, book={self.book.title}, qty={self.quantity})"


class Payment(models.Model):
    """Payment model to track Flutterwave transactions."""
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payments')
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE, related_name='payment', null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, help_text="Amount in Naira")
    currency = models.CharField(max_length=10, default='NGN')
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    # Flutterwave transaction ID
    flutterwave_txn_id = models.CharField(max_length=255, unique=True, null=True, blank=True, help_text="Flutterwave transaction ID")
    flutterwave_ref = models.CharField(max_length=255, unique=True, null=True, blank=True, help_text="Flutterwave reference")
    
    # Payment method
    payment_method = models.CharField(max_length=50, default='card', help_text="Card, Transfer, USSD, etc.")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True, help_text="When payment was completed")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
    
    def __str__(self):
        return f"Payment #{self.payment_id} - {self.customer.name} - ₦{self.amount} ({self.status})"
    
    def __repr__(self):
        return f"Payment(id={self.payment_id}, customer={self.customer.name}, amount={self.amount}, status='{self.status}')"
