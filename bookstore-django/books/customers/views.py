from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import Customer
from .serializers import CustomerSerializer, SignUpSerializer, LoginSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Customer model.
    Provides CRUD operations and authentication endpoints.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Users can only see their own customer profile."""
        if self.request.user.is_staff:
            return Customer.objects.all()
        return Customer.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def signup(self, request):
        """Create a new customer account."""
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response(
                {
                    'message': 'Account created successfully',
                    'customer': CustomerSerializer(customer).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        """Authenticate a customer."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                
                if user is not None:
                    auth_login(request, user)
                    customer = Customer.objects.get(user=user)
                    return Response(
                        {
                            'message': 'Login successful',
                            'customer': CustomerSerializer(customer).data,
                            'user_id': user.id,
                        },
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {'error': 'Invalid credentials'},
                        status=status.HTTP_401_UNAUTHORIZED
                    )
            except User.DoesNotExist:
                return Response(
                    {'error': 'User not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        """Logout a customer."""
        auth_logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        """Get current customer profile."""
        try:
            customer = Customer.objects.get(user=request.user)
            serializer = self.get_serializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(
                {'error': 'Customer profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )
