from django.contrib import admin
from .models import Book, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'title', 'author', 'category', 'price', 'created_at']
    list_filter = ['author', 'category', 'price', 'created_at']
    search_fields = ['title', 'author']
    ordering = ['-created_at']
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'description', 'category', 'price')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
