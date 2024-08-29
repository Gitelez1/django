from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"

class Order(models.Model):
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: ${self.total_price} ({self.total_quantity} items)"
