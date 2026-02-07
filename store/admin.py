from django.contrib import admin
from .models import Category, Customer, Product, Order, OrderItem


# Register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']
    search_fields = ['category_name']


# Register Customer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_name', 'contact_number', 'age']
    search_fields = ['customer_name']


# Register Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'price', 'category']
    search_fields = ['product_name']
    list_filter = ['category']


# Register Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer', 'product', 'order_date', 'quantity']
    list_filter = ['order_date']


# Register OrderItem
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_item_id', 'order', 'product']

    admin.site.site_header = "Ocharon"
    admin.site.site_title = "Ocharon Admin"
    admin.site.index_title = "Dashboard"

