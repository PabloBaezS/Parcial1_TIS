from django.db import models

# Create your models here.

class Flight(models.Model):
    TYPE_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]

    name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.flight_type}"