from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('place_booking/<int:hostel_id>/', views.place_booking, name='place_booking'),
     path('booking_completed/<int:listing_id>/', views.booking_completed, name='booking_completed'),
    path('process/<str:ref>/', views.verify_payment, name='verify-payment'),
    
]