import uuid
from django.conf import settings
from django.db import models
from manageusers.models import User

# Model to store different categories or specialties for doctors.
class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name_category

# Model for storing doctor-specific information and profile details.
class DoctorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    practice_name = models.CharField(max_length=255)
    bio = models.TextField()  # A brief biography or description of the doctor
    services_offered = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # The doctor's specialization
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    city = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Model for doctors rating
    # Models for showing the map