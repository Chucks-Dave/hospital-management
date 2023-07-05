from email.policy import default
from random import choices
from django.db import models
from user_auth.models import User



# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="doctor_appointments", null=True)
    reason = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    
    def __str__(self):
        return self.reason


class Ailment(models.Model):
    danger_levels = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('very_high', 'Very High'),
        ('critical', 'Critical'),
    ]
    
    name = models.CharField(max_length=200)
    danger_level = models.CharField(max_length=100, choices=danger_levels)
    symptoms = models.TextField()
    prescription = models.TextField()
    
    affects_brain = models.BooleanField(default=False)
    affects_lungs = models.BooleanField(default=False)
    affects_heart = models.BooleanField(default=False)
    affects_liver = models.BooleanField(default=False)
    affects_stomach = models.BooleanField(default=False)
    affects_intestine = models.BooleanField(default=False)
    affects_kindeys = models.BooleanField(default=False)
    affects_other = models.BooleanField(default=False)
    other = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    