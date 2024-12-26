
import uuid

from django.conf import settings
from django.db import models
from users.models import User

# Doctor profile models goes here
class DoctorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    practice_name = models.CharField(max_length=255)
    bio = models.TextField()
    services_offered = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    #city
    #town
    #province
    image = models.ImageField(upload_to='uploads/listing')
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'

"""
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    # Links the profile to a specific user.
    address = models.TextField(null=False)
    # The address field stores the doctor's address information
    services = models.TextField()
    # A services field to store a list or description of the services provided by the doctor.
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

# Categories model goes here
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Patient models goes here
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    # Links the profile to a specific user. Each user can have only one PatientProfile.

# Doctor models goes here
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    # Links the profile to a specific user.
    address = models.TextField(null=False)
    # The address field stores the doctor's address information
    services = models.TextField()
    # A services field to store a list or description of the services provided by the doctor.
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

# Appointment models goes here
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateField()
    time = models.TimeField()
"""