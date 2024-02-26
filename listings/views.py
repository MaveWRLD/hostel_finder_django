import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hostels.models import Hostel
from .forms import ListingCreateForm
from .models import ListingItem



@login_required
def place_booking(request, hostel_id):
    # Get the specific hostel
    hostel = get_object_or_404(Hostel, id=hostel_id)

    if request.method == 'POST':
        form = ListingCreateForm(request.POST)
        if form.is_valid():
            listing = form.save()

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            booking_number = current_date + str(listing.id)
            listing.booking_number = booking_number
            listing.save()
        


            # Create a ListingItem instance for the specific hostel
            ListingItem.objects.create(
                listing=listing,  # associate the item with the new listing
                hostel=hostel,
                price=hostel.hostel_price,  # replace with the actual price field of your Hostel model
            )

            request.session['booking_number'] = booking_number
            #return redirect(reverse('payment:process'))
            return render(request, 'listings/booking_completed.html', {'listing': listing, 'hostel': hostel })

    form = ListingCreateForm()
    return render(request, 'listings/place_booking.html', {'form': form, 'hostel': hostel})