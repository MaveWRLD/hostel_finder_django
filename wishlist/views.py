from django.shortcuts import render, get_object_or_404, redirect
from hostels.models import Hostel
from .models import Wishlist, WishListItems


def _wishlist_id(request):
    wishlist = request.session.session_key
    if not wishlist:
         request.session.create()
        wishlist = request.session.session_key
    return wishlist


def add_wishlist(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    
    # Check if a wishlist already exists for this user
    wishlist, created = Wishlist.objects.get_or_create(wishlist_id=_wishlist_id(request))
    
    # Check if the hostel is already in the wishlist items
    wishlist_item, created = WishListItems.objects.get_or_create(hostels=hostel, wishlist=wishlist)

    return redirect('wishlist:wishlist')

def wishlist(request):
    return render(request, 'wishlist/wishlist.html')
# Create your views here.
