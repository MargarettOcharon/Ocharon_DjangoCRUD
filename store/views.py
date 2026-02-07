from rest_framework import viewsets
from .models import Category, Customer, Product, Order, OrderItem
from .serializers import (
    CategorySerializer, 
    CustomerSerializer, 
    ProductSerializer, 
    OrderSerializer, 
    OrderItemSerializer
)


# View 1: Category CRUD
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Category CRUD operations
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# View 2: Customer CRUD
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Customer CRUD operations
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# View 3: Product CRUD
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Product CRUD operations
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# View 4: Order CRUD
class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Order CRUD operations
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# View 5: OrderItem CRUD
class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for OrderItem CRUD operations
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer