from django.contrib import admin
from hotel.models import Bill, Booking, Hotel, Menu,Room
# Register your models here.

admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Bill)
admin.site.register(Hotel)
admin.site.register(Menu)