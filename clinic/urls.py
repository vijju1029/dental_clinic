from django.urls import path, include
from rest_framework import routers
from .views import PatientViewSet, AppointmentViewSet, InventoryViewSet, home

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'inventory', InventoryViewSet)

urlpatterns = [
    path('', home),
    path('api/', include(router.urls)),
]
