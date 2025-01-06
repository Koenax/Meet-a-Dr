from rest_framework import serializers
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest
from manageusers.serializers import UserDetailsSerializer

class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Patient model.
    Provides a nested UserDetailsSerializer for the user field 
    and a read-only age field.
    """
    user = UserDetailsSerializer(read_only=True, many=False)  # Nested serializer for user details
    age = serializers.ReadOnlyField()  # Read-only calculated age field

    class Meta:
        model = Patient
        fields = (
            'id',              # Unique identifier
            'user',            # Related user details
            'first_name',      # Patient's first name
            'last_name',       # Patient's last name
            'date_of_birth',   # Date of birth
            'age',             # Calculated age (read-only)
            'gender',          # Gender of the patient
            'contact_number',  # Contact number
            'email',           # Email address
        )


class HealthHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for the HealthHistory model.
    Includes a read-only patient_name field derived from the Patient model's first_name.
    """
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)  # Read-only field for patient name

    class Meta:
        model = HealthHistory
        fields = (
            'id',                   # Unique identifier
            'patient',              # Related patient ID
            'patient_name',         # Patient's first name (read-only)
            'medical_conditions',   # Medical conditions
            'allergies',            # Known allergies
            'current_medications',  # Current medications
            'previous_surgeries',   # Details of past surgeries
            'family_history',       # Family medical history
        )


class TreatmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Treatment model.
    Includes a read-only patient_name field derived from the Patient model's first_name.
    """
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)  # Read-only field for patient name

    class Meta:
        model = Treatment
        fields = (
            'id',               # Unique identifier
            'patient',          # Related patient ID
            'patient_name',     # Patient's first name (read-only)
            'treatment_name',   # Name of the treatment
            'date',             # Date of the treatment
            'description',      # Description of the treatment
        )


class DiagnosisSerializer(serializers.ModelSerializer):
    """
    Serializer for the Diagnosis model.
    Includes a read-only patient_name field derived from the Patient model's first_name.
    """
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)  # Read-only field for patient name

    class Meta:
        model = Diagnosis
        fields = (
            'id',               # Unique identifier
            'patient',          # Related patient ID
            'patient_name',     # Patient's first name (read-only)
            'diagnosis_name',   # Name of the diagnosis
            'date',             # Date of the diagnosis
            'notes',            # Additional notes or observations
        )


class ScreeningTestSerializer(serializers.ModelSerializer):
    """
    Serializer for the ScreeningTest model.
    Includes a read-only patient_name field derived from the Patient model's first_name.
    """
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)  # Read-only field for patient name

    class Meta:
        model = ScreeningTest
        fields = (
            'id',               # Unique identifier
            'patient',          # Related patient ID
            'patient_name',     # Patient's first name (read-only)
            'test_name',        # Name of the screening test
            'date',             # Date of the test
            'result',           # Test result
            'notes',            # Additional notes or observations
        )
