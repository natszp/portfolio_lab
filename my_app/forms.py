from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

from .models import *
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': 'form-group'}))
    password = forms.CharField(label='password', max_length=120,
                               widget=forms.PasswordInput(attrs={'class': 'form-group'}))
    password2 = forms.CharField(label='repeat password', max_length=120,
                               widget=forms.PasswordInput(attrs={'class' : 'form-group'}))

class LoginForm(forms.Form):
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': 'form-group'}))
    password = forms.CharField(label='password', max_length=120,
                               widget=forms.PasswordInput(attrs={'class': 'form-group'}))

class DonationForm(forms.Form):
    categories = forms.MultipleChoiceField(choices=Category)
    quantity = forms.IntegerField()
    institution = forms.CheckboxInput()
    address = forms.Textarea()
    zip_code = forms.CharField()
    phone_number = forms.IntegerField()
    pick_up_date = forms.DateField()
    pick_up_time = forms.TimeField()
    pick_up_comment = forms.Textarea()



