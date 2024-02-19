from django.contrib import admin
from .models import Wishlist, WishListItems

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['wishlist_id', 'date_added']
    list_filter = ['date_added']
    ordering = ('date_added',)
    

@admin.register(WishListItems)
class WishlistItemsAdmin(admin.ModelAdmin):
    list_display = ['hostels', 'wishlist', 'is_active']
    list_filter = ['hostels']
    ordering = ('hostels',)
    




# Register your models here.
