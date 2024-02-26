from django.contrib import admin
from .models import Listing, ListingItem

class ListingItemInline(admin.TabularInline):
    model = ListingItem
    raw_id_fields = ['hostel']

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','booking_number',
    'address', 'paid',
    'created', 'updated']
    list_filter = ['paid', 'created', 'updated', 'booking_number']
    inlines = [ListingItemInline]
# Register your models here.
