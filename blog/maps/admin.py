from django.contrib import admin
from models import VehicleLocation

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    fields = ['latitude', 'longitude', 'angle', 'date_time']
    list_display = ('date_time','latitude', 'longitude', 'angle')

admin.site.register(VehicleLocation, LocationAdmin)
