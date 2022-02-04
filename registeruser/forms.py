from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import myUser
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

ERROR_MESSAGE = _("Please enter a correct email and password. ")
ERROR_MESSAGE_RESTRICTED = _("You do not have permission to access the admin.")
ERROR_MESSAGE_INACTIVE = _("This account is inactive.")

class registerUser(UserCreationForm):
    class Meta:
        model = myUser
        fields = ("username", "email", "password1", "password2")


  
class AuthenticationForm(forms.Form): # Note: forms.Form NOT forms.ModelForm
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email','placeholder':'Email'}), 
        label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
        label='Password')

    class Meta:
        fields = ['email', 'password']