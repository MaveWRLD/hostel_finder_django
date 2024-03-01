import datetime
import uuid
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from hostels.models import Hostel
from .models import Listing
from .forms import ListingCreateForm


@login_required
def place_booking(request: HttpRequest, hostel_id) -> HttpResponse:
    hostel = get_object_or_404(Hostel, id=hostel_id)
    pk = settings.PAYSTACK_PUBLIC_KEY
    if request.method == 'POST':
        form = ListingCreateForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            # listing.hostel_price = hostel.hostel_price
            listing.hostel_name = hostel.hostel_name
            listing.hostel_price = hostel.hostel_price
            listing.save()

            # Set booking number in session
            # yr = datetime.date.today().strftime('%Y')
            # mt = datetime.date.today().strftime('%m')
            # dt = datetime.date.today().strftime('%d')
            # current_date = f"{yr}{mt}{dt}"
            # unique_id = uuid.uuid4().hex[:6]
            # booking_number = f"{current_date}-{listing.id}-{unique_id}"
            # request.session['booking_number'] = booking_number

            return render(request, 'listings/process.html', {'listing': listing, 'pk': pk})
    else:
        form = ListingCreateForm()
    return render(request, 'listings/place_booking.html', {'form': form, 'hostel': hostel})


def verify_payment(request, ref):
    listing = Listing.objects.get(ref=ref)
    paid = listing.verify_payment()
    if paid:
        messages.success(request, 'Payment successful')
    else:
        messages.error(request, 'Payment not successful')
    return redirect('listing:booking_completed', listing_id=listing.id)


def booking_completed(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/booking_completed.html', {'listing': listing})
