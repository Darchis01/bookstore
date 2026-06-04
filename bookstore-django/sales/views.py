from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Sale
from .serializers import SaleSerializer, SaleCreateSerializer
from customers.models import Customer


class SaleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Sale model.
    Provides CRUD operations for sales/orders.
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['customer', 'book', 'date']
    ordering_fields = ['date', 'total_price']

    def get_queryset(self):
        """Users can only see their own sales."""
        if self.request.user.is_staff:
            return Sale.objects.all()
        try:
            customer = Customer.objects.get(user=self.request.user)
            return Sale.objects.filter(customer=customer)
        except Customer.DoesNotExist:
            return Sale.objects.none()

    def get_serializer_class(self):
        """Use different serializers for different actions."""
        if self.action == 'create':
            return SaleCreateSerializer
        return SaleSerializer

    def create(self, request, *args, **kwargs):
        """Create a new sale for the current customer."""
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            return Response(
                {'error': 'Customer profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            sale = serializer.save(customer=customer)
            return Response(
                SaleSerializer(sale).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def my_orders(self, request):
        """Get all orders for the current customer."""
        try:
            customer = Customer.objects.get(user=request.user)
            sales = Sale.objects.filter(customer=customer).order_by('-date')
            serializer = self.get_serializer(sales, many=True)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(
                {'error': 'Customer profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['get'])
    def order_summary(self, request):
        """Get summary of orders for the current customer."""
        try:
            customer = Customer.objects.get(user=request.user)
            sales = Sale.objects.filter(customer=customer)
            
            total_orders = sales.count()
            total_spent = sum(sale.total_price for sale in sales)
            total_books = sum(sale.quantity for sale in sales)
            
            return Response({
                'total_orders': total_orders,
                'total_spent': str(total_spent),
                'total_books_purchased': total_books,
            })
        except Customer.DoesNotExist:
            return Response(
                {'error': 'Customer profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )
