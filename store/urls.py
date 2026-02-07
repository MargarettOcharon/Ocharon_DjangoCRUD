from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    CustomerViewSet,
    ProductViewSet,
    OrderViewSet,
    OrderItemViewSet
)

# Create router
router = DefaultRouter()

# Register viewsets
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='orderitem')

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
]