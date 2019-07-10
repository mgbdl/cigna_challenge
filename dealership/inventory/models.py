from django.db import models
from datetime import datetime

import uuid

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=200)
    doors = models.IntegerField()
    lot_number = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.lot_number} - {self.model}'
