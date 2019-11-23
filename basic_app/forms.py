from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserContacts


class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserContactForm(forms.ModelForm):

    class Meta():
        model = UserContacts
        fields = ['first_name', 'last_name', 'phone_number','email_address','street_address']
