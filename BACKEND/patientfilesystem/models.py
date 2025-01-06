import uuid
from django.db import models
from manageusers.models import User

class Patient(models.Model):
    """
    Represents a patient in the healthcare system.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)  # Patient's first name
    last_name = models.CharField(max_length=100)   # Patient's last name
    date_of_birth = models.DateField()             # Patient's date of birth
    age = models.IntegerField(blank=True, null=True)  # Calculated age (optional)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    )  # Gender of the patient
    contact_number = models.CharField(max_length=15)  # Contact number of the patient
    email = models.EmailField()                      # Email address of the patient
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp of last update

    def save(self, *args, **kwargs):
        """
        Overridden save method to calculate age if not provided.
        """
        if not self.age:
            from datetime import date
            today = date.today()
            self.age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        super().save(*args, **kwargs)

class HealthHistory(models.Model):
    """
    Stores the health history of a patient.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='health_histories'
    )  # Related patient
    medical_conditions = models.TextField()  # Patient's medical conditions
    allergies = models.TextField()           # Allergies of the patient
    current_medications = models.TextField() # Current medications
    previous_surgeries = models.TextField()  # Details of past surgeries
    family_history = models.TextField()      # Family medical history
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Treatment(models.Model):
    """
    Represents treatments received by a patient.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(
        Patient, related_name='treatments', on_delete=models.CASCADE
    )  # Related patient
    treatment_name = models.CharField(max_length=200)  # Name of the treatment
    date = models.DateField()                          # Date of the treatment
    description = models.TextField()                  # Description of the treatment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Diagnosis(models.Model):
    """
    Represents a diagnosis for a patient.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='diagnoses'
    )  # Related patient
    diagnosis_name = models.CharField(max_length=200)  # Name of the diagnosis
    date = models.DateField()                          # Date of the diagnosis
    notes = models.TextField()                         # Additional notes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScreeningTest(models.Model):
    """
    Represents screening tests conducted on a patient.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='screening_tests'
    )  # Related patient
    test_name = models.CharField(max_length=200)  # Name of the test
    date = models.DateField()                     # Date of the test
    result = models.TextField()                   # Test result details
    notes = models.TextField()                    # Additional notes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
