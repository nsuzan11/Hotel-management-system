from django.contrib import admin
from django.urls import path
from hotel.views import index
from django.urls import include
from .views import index,aboutus,rooms,login,book,contactus

app_name = 'hotel'
urlpatterns = [
    path('', index),
    path('hotel/aboutus', aboutus),
    path('hotel/rooms', rooms),
    path('hotel/book', book),
    path('hotel/contactus', contactus),
    path('hotel/login', login),

]
