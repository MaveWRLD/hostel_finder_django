from django.db import models
from django.urls import reverse

class Location(models.Model):
    location_name = models.CharField(max_length=250)
    slug = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.location_name}'
    
    def get_absolute_url(self):
        return reverse("hostels:hostels_by_location", args=[self.slug])
    
# Create your models here.
