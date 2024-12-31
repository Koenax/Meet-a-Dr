from rest_framework import serializers
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest
from manageusers.serializers import UserDetailsSerializer

class PatientSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True, many=False)
    age = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = (
            'id',
            'user',
            'first_name',
            'last_name',
            'date_of_birth', 
            'age',
            'gender',
            'contact_number',
            'email',
        )


class HealthHistorySerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)

    class Meta:
        model = HealthHistory
        fields = (
            'id',
            'patient',
            'patient_name',
            'medical_conditions', 
            'allergies',
            'current_medications',
            'previous_surgeries', 
            'family_history',
        )

class TreatmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)

    class Meta:
        model = Treatment
        fields = (
            'id',
            'patient',
            'patient_name',
            'treatment_name', 
            'date',
            'description',
        )
            

class DiagnosisSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)

    class Meta:
        model = Diagnosis
        fields = (
            'id',
            'patient',
            'patient_name',
            'diagnosis_name', 
            'date',
            'notes',
        )         

class ScreeningTestSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)

    class Meta:
        model = ScreeningTest
        fields = (
            'id',
            'patient',
            'patient_name',
            'test_name', 
            'date',
            'result',
            'notes',
        )
