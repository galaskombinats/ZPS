from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, PrescriptionViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
