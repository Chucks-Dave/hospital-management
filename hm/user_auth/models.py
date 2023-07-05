from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    staff_types = [
        ('none', 'None'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    ]
    areas = [
        ('', ''),
        ('Cardiologists', 'Cardiologists'),
        ('Dermatologists', 'Dermatologists'),
        ('Gynecologists', 'Gynecologists'),
        ('Pediatricians', 'Pediatricians'),
        ('Ophthalmologists', 'Ophthalmologists'),
        ('General Surgeons', 'General Surgeons'),
    ]

    staff_type = models.CharField(
        max_length=50, choices=staff_types, default="none")
    area_of_specialization = models.CharField(
        max_length=100, blank=True, null=True, choices=areas)
    phone = models.CharField(max_length=15, null=True, blank=True)
