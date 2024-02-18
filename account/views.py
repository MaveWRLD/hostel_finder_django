from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'account:dashbord')

    else:
        form = UserRegisterForm()
    return render(request, 'hostels/register.html', {'form': form})


def index(request):
    return render(request, 'hostels/index.html')


@login_required
def dashboard(request):
    return render(request, 'hostels/dashboard.html', {'section': 'dashboard'})


def logout_user(request):
    logout(request)
    return redirect('login')
# Create your views here.
