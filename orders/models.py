from django.db import models
from home.models import Product
from django.contrib.auth import get_user_model


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Mets:
        ordering = ('paid','-updated')
        
    def __str__(self):
        return f"{self.id} - {self.updated}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    price    = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity