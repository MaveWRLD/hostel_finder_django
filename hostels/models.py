from django.db import models
from django.contrib.auth.models import User
from category.models import Location
from django.urls import reverse


class HostelAvailable(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=200)
    hostel_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    slug = models.CharField(max_length=400,  unique=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    hostel_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel_price = models.DecimalField(max_digits=15, decimal_places=2)
    hostel_description = models.TextField()
    hostel_image = models.ImageField(upload_to='hostel_main_image')
    hostel_bedroom = models.ImageField(upload_to='hostel_bedroom', blank=True)
    hostel_kitchen = models.ImageField(upload_to='hostel_kitchen', blank=True)
    hostel_washroom = models.ImageField(
        upload_to='hostel_washroom', blank=True)

    objects = models.Manager()
    hostelAvailable = HostelAvailable()
    
    def __str__(self):
        return f'{self.hostel_name}'
    
    def get_absolute_url(self):
        return reverse("hostels:hostel_details", args=[self.created_date.year,
                                                     self.created_date.month,
                                                     self.created_date.day,
                                                     self.slug])
    
# Create your models here.
