from django.urls import path
from . import views

app_name = 'hostels'

urlpatterns = [
    path('', views.index, name='home_page'),
    path('hostels/', views.hostel, name='hostels'),
    path('location/<int:year>/<int:month>/<int:day>/<slug:hostel>/',
         views.hostel_details, name='hostel_details'),
    path('location/<slug:location>/',views.hostel, name='hostels_by_location'),
    path('search/', views.search, name = 'search'),
]
