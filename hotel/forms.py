from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# import email

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

# 'checkin','checkout','roomtype','nopeople','phonenumber'
# class BookForm(forms.Form):
#     fullname = forms.CharField(max_length=100)
#     checkin = forms.DateField()
#     checkout = forms.DateField()
#     roomtype = forms.CharField(max_length=100)
#     nopoeple = forms.IntegerField()
#     email = forms.EmailField()
#     phone_number = forms.IntegerField()