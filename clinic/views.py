from rest_framework import viewsets
from .models import Patient, Appointment, Inventory
from .serializers import PatientSerializer, AppointmentSerializer, InventorySerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# For root URL response
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to the Dental Clinic Management System!")
