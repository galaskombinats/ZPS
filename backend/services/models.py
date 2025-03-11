from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    manufacturer = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    requires_prescription = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    dosage_instructions = models.TextField()

    def __str__(self):
        return f"Prescription for {self.patient.username} - {self.medicine.name}"
    
class Order(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.patient.username}"
    