from django.db import models

# Create your models here.

class Monowheel(models.Model):
    brand = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    max_speed = models.FloatField(null=True)
    range = models.FloatField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.brand} {self.model}"