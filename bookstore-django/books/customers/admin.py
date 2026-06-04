from django.contrib import admin
from .models import Customer, Wishlist


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'email', 'phone', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'email', 'phone']
    ordering = ['-created_at']
    fieldsets = (
        ('Customer Information', {
            'fields': ('user', 'name', 'email', 'phone')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['wishlist_id', 'user', 'books_count', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'user__email']
    filter_horizontal = ['books']
    ordering = ['-created_at']
    fieldsets = (
        ('Wishlist Information', {
            'fields': ('user', 'books')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = 'Books in Wishlist'
