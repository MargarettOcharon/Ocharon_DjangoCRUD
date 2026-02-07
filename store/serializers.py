from rest_framework import serializers
from .models import Category, Customer, Product, Order, OrderItem


# Serializer 1: Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name']


# Serializer 2: Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'customer_name', 'customer_address', 
                  'contact_number', 'age']


# Serializer 3: Product
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.category_name', 
        read_only=True
    )
    
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'manufacture_date', 
                  'exp_date', 'description', 'price', 'category', 
                  'category_name']


# Serializer 4: Order
class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source='customer.customer_name', 
        read_only=True
    )
    product_name = serializers.CharField(
        source='product.product_name', 
        read_only=True
    )
    
    class Meta:
        model = Order
        fields = ['order_id', 'product', 'customer', 'order_date', 
                  'quantity', 'customer_name', 'product_name']


# Serializer 5: OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source='product.product_name', 
        read_only=True
    )
    
    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'product', 'order', 'product_name']