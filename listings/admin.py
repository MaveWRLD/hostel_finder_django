from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'hostel_name', 'hostel_price', 'address', 'paid',
    'created', 'updated']
    list_filter = ['hostel_name', 'paid', 'created', 'updated']
# Register your models here.
