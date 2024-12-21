from django.db import models
from django.contrib.auth.models import User

# Patient modules goes here
Class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Patient_profile')
    bio = models.TextField(blank=True)
    preferences = models.JSONField(default=dict)

# Doctor modules goes here
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    bio = models.TextField(blank=True)
    address = models.TextField(null=True)
    availability = models.JSONField(default=dict)
    services = models.TextField()
