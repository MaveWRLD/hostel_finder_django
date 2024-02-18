from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationRegister(admin.ModelAdmin):
    list_display = ['location_name', 'description']
    prepopulated_fields = {'slug': ['location_name']}
# Register your models here.
