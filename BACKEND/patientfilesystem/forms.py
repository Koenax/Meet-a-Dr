from django import forms
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'user',
            'first_name',
            'last_name',
            'date_of_birth', 
            'gender',
            'contact_number',
            'email',
        )

class HealthHistoryForm(forms.ModelForm):
    class Meta:
        model = HealthHistory
        fields = (
            'patient',
            'medical_conditions',
            'allergies', 
            'current_medications',
            'previous_surgeries',
            'family_history'
        )

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = (
            'patient',
            'treatment_name',
            'date',
            'description',
        )


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = (
            'patient',
            'diagnosis_name',
            'date',
            'notes',
            )

class ScreeningTestForm(forms.ModelForm):
    class Meta:
        model = ScreeningTest
        fields = (
            'patient',
            'test_name',
            'date',
            'result',
            'notes',
        )
            