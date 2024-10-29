from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    STATUS_CHOICES = [
        ('S', 'Success'),
        ('D', 'Declined'),
        ]

    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='S')

    def __str__(self):
        return f"Payment #{self.id} by {self.customer.first_name} {self.customer.last_name}"

