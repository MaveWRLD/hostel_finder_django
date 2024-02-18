from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.register, name='register'),
     path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout_user, name='logout'),
]
