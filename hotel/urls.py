from django.contrib import admin
from django.urls import path
from hotel.views import index
from django.urls import include
from .views import index,aboutus,rooms,login,book,contactus

app_name = 'hotel'
urlpatterns = [
    path('', index),
    path('aboutus.html', aboutus),
    path('rooms.html', rooms),
    path('book.html', book),
    path('contactus.html', contactus),
    path('login.html', login),

]
