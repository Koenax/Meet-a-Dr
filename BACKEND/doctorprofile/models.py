import uuid
from django.conf import settings
from django.db import models
from django.contrib.gis.db import models  # For handling geographic data
from manageusers.models import User  # Importing the custom User model

class DoctorProfile(models.Model):
    """
    Represents a doctor's profile with important information.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique identifier for each doctor profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')  # Links the profile to a specific user account
    practice_name = models.CharField(max_length=255)  # Name of the doctor's practice or clinic
    bio = models.TextField()  # A brief biography of the doctor
    services_offered = models.TextField()  # Description of services provided
    category = models.CharField(max_length=255)  # Doctor's specialization
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)  # Fee charged for consultations
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Average rating given by clients (e.g., 4.5)
    city = models.CharField(max_length=255, blank=True, null=True)  # City where the doctor practices
    town = models.CharField(max_length=255, blank=True, null=True)  # Town where the doctor practices
    province = models.CharField(max_length=255, blank=True, null=True)  # Province or state where the doctor practices
    hpcsa_registration_number = models.CharField(max_length=20, unique=True)  # Unique number for Health Professions Council registration
    is_verified = models.BooleanField(default=False)  # Indicates whether the profile is verified by admins
    location = models.PointField(geography=True, blank=True, null=True)  # GeoDjango PointField to store geographical location
    image = models.ImageField(upload_to='uploads/doctorprofile')
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the profile was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update to the profile