from django.shortcuts import render, get_object_or_404
from category.models import Location
from .models import Hostel



def index(request):
    hostels = Hostel.hostelAvailable.all()
    return render(request, 'hostels/index.html', {'hostels': hostels})


def hostel_details(request, year, month, day, hostel):
    hostels = get_object_or_404(
        Hostel,
        created_date__year=year,
        created_date__month=month,
        created_date__day=day,
        slug=hostel,
        is_available=True,
    )
    return render(request, 'hostels/hostel_details.html', {'hostels': hostels})


def hostel(request, location=None):
    hostels = Hostel.hostelAvailable.all()
    if location:
        location_obj = get_object_or_404(Location, slug=location)
        hostels = hostels.filter(hostel_location=location_obj)
    return render(request, 'hostels/hostels.html', {'hostels': hostels})
# Create your views here.
