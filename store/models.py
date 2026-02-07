from django.db import models


# Model 1: Category
class Category(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


# Model 2: Customer
class Customer(models.Model):
    customer_id = models.BigIntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.customer_name


# Model 3: Product
class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    manufacture_date = models.DateField()
    exp_date = models.DateField()
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        db_column='category_id'
    )

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name


# Model 4: Order
class Order(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product_id'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        db_column='cust_id'
    )
    order_date = models.DateField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f"Order {self.order_id}"


# Model 5: OrderItem
class OrderItem(models.Model):
    order_item_id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product_id'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        db_column='order_id'
    )

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return f"Order Item {self.order_item_id}"