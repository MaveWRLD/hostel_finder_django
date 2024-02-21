from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:hostel_id>/', views.add_wishlist, name='add_wishlist'),
    path('remove_wishlist_item/<int:hostel_id>/', views.remove_wishist_item, name='remove_wishlist_item')
]
