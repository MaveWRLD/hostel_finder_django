from django.db import models
from hostels.models import Hostel



class Listing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    booking_number = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
        models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class ListingItem(models.Model):
    listing = models.ForeignKey(Listing, related_name='items', on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
    decimal_places=2)
    
    def __str__(self):
        return str(self.id)
        
    def get_cost(self):
        return self.price * self.quantity

# Create your models here.
