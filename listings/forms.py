from django import forms
from .models import Listing
class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['first_name', 'last_name', 'email', 'address']  