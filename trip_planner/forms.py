from socket import fromshare
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Trip


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = "date"


class DateForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ["location", "description", "packing", "startDate", "endDate", ]
        widgets = {"my_date_field": DateInput()}
