from django.contrib import admin
from .models import Patient, Appointment, Inventory

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Inventory)
