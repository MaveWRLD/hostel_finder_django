from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:hostel_id>/', views.add_wishlist, name='add_wishlist')
]
