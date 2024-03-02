from django.urls import path
from django.contrib.auth import views as authView
from . import views

app_name = 'account'

urlpatterns = [
     path('login/', authView.LoginView.as_view(), name='login'),
     path('register', views.register, name='register'),
     path('logout', views.logout_user, name='logout'),
     path('dashboard/', views.dashboard, name='dashboard'),
]
