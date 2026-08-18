from django.contrib import admin
from .models import Sale, Payment


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['sale_id', 'customer', 'book', 'quantity', 'total_price', 'date']
    list_filter = ['date', 'customer', 'book']
    search_fields = ['customer__name', 'book__title', 'sale_id']
    ordering = ['-date']
    fieldsets = (
        ('Sale Information', {
            'fields': ('customer', 'book', 'quantity', 'total_price')
        }),
        ('Transaction Details', {
            'fields': ('date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['total_price', 'date', 'created_at', 'updated_at']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'customer', 'amount', 'status', 'flutterwave_ref', 'created_at']
    list_filter = ['status', 'created_at', 'payment_method']
    search_fields = ['customer__name', 'flutterwave_ref', 'flutterwave_txn_id']
    ordering = ['-created_at']
    fieldsets = (
        ('Payment Information', {
            'fields': ('customer', 'sale', 'amount', 'currency', 'status')
        }),
        ('Flutterwave Details', {
            'fields': ('flutterwave_txn_id', 'flutterwave_ref', 'payment_method'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['flutterwave_txn_id', 'flutterwave_ref', 'created_at', 'updated_at', 'completed_at']
