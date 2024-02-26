from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from listings.models import Listing

# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request):
    booking_number = request.session.get('booking_number', None)
    listing = get_object_or_404(Listing, id=booking_number)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        # Stripe checkout session data
        session_data = {
        'mode': 'payment',
        'client_reference_id': listing.booking_number,
        'success_url': success_url,
        'cancel_url': cancel_url,
        'line_items': []
        }

        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)
    else:
        return render(request, 'payment/process.html', )

# Create your views here.
