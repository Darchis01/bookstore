from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer
from books.customers.models import Wishlist


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model.
    Provides CRUD operations and filtering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['author', 'price']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'price', 'created_at']

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available books."""
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_price(self, request):
        """Get books within a price range."""
        min_price = request.query_params.get('min_price', 0)
        max_price = request.query_params.get('max_price', 999999)
        
        books = self.get_queryset().filter(price__gte=min_price, price__lte=max_price)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def toggle_wishlist(self, request, pk=None):
        """Toggle a book in the user's wishlist."""
        try:
            book = self.get_object()
            user = request.user
            
            # Get or create wishlist for user
            wishlist, created = Wishlist.objects.get_or_create(user=user)
            
            # Toggle book in wishlist
            if wishlist.books.filter(pk=book.pk).exists():
                wishlist.books.remove(book)
                in_wishlist = False
            else:
                wishlist.books.add(book)
                in_wishlist = True
            
            return Response({
                'status': 'success',
                'in_wishlist': in_wishlist,
                'wishlist_count': wishlist.books.count(),
                'message': f'Book {"added to" if in_wishlist else "removed from"} wishlist'
            })
        except Book.DoesNotExist:
            return Response(
                {'error': 'Book not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
