from django.contrib import admin
from .models import Hostel

@admin.register(Hostel)
class HostelRegister(admin.ModelAdmin):
    list_display = ['hostel_name', 'hostel_location', 'hostel_manager','hostel_price', 'stock','created_date', 'is_available']
    list_filter = ['hostel_price', 'hostel_location', 'stock', 'is_available']
    ordering = ('hostel_price',)
    prepopulated_fields = {'slug':('hostel_name',)}

# Register your models here.
