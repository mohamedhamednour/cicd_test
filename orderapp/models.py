from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Offer(models.Model):

    name = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="offers")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


# class Order(models.Model):
#     """
#     Order model.
#     """
#     user = models.ForeignKey('userapp.User', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     items_order = models.ManyToManyField(Book, through='OrderItem')
#     objects = managers.OrderManager.as_manager()


#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"Order {self.id} by {self.user}"


# class Cart(models.Model):
#     """
#     Cart model.
#     """
#     user = models.ForeignKey('userapp.User', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     objects = managers.CartManager.as_manager()


#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"Cart {self.id} for {self.user}"

# class CartItem(models.Model):
#     """
#     CartItem model.
#     """
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     class Meta:
#         unique_together = ('cart', 'book')


#     def __str__(self):
#         return f"CartItem {self.id} for {self.cart}"

# class OrderItem(models.Model):
#     """
#     OrderItem model.
#     """
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)


#     def __str__(self):
#         return f"OrderItem {self.id} for {self.order}"
