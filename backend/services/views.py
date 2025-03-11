from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .models import Medicine, Prescription, Order
from .serializers import MedicineSerializer, PrescriptionSerializer, OrderSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ✅ Medicine CRUD (Read-only for unauthenticated users, full access for authenticated users)
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ✅ Prescription CRUD (Same as Medicine)
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ✅ Order CRUD (Handled entirely by this viewset)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ✅ User Registration (Anyone can register)
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
