from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    hostels_list = Hostel.hostelAvailable.all()

    if location:
        location_obj = get_object_or_404(Location, slug=location)
        hostel_p = hostels_list.filter(hostel_location=location_obj)
    else:
        hostel_p = hostels_list

    paginator = Paginator(hostel_p, 3)
    page_number = request.GET.get('page')

    try:
        hostels = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hostels = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hostels = paginator.page(paginator.num_pages)

    return render(request, 'hostels/hostels.html', {'hostels': hostels})

def search(request):
    return render(request, 'hostels/hostels.html')
# Create your views here.
