from django.db import models
from hostels.models import Hostel

class Wishlist(models.Model):
    wishlist_id = models.CharField(max_length = 250)
    date_added = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.wishlist_id}'
    
    objects = models.Manager()
    

class WishListItems(models.Model):
    hostels = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.hostels}'
    
    objects = models.Manager()
# Create your models here.
