from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('place_booking/<int:hostel_id>/', views.place_booking, name='place_booking'),
]