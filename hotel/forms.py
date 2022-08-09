from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Booking
# import email

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user_info']
        fields = ('room_type','start_day','end_day','no_people','phone_number','email')
        widgets = {
            'start_day' : DatePickerInput(),
            'end_day' : DatePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user_info = kwargs.pop('user_info', None)
        super(BookingForm, self).__init__(*args, **kwargs)

# 'checkin','checkout','roomtype','nopeople','phonenumber'
# class BookForm(forms.Form):
#     fullname = forms.CharField(max_length=100)
#     checkin = forms.DateField()
#     checkout = forms.DateField()
#     roomtype = forms.CharField(max_length=100)
#     nopoeple = forms.IntegerField()
#     email = forms.EmailField()
#     phone_number = forms.IntegerField()