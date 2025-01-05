from django import forms
from .models import DoctorProfile

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = (
            'practice_name',
            'bio',
            'services_offered',
            'category',
            'consultation_fee',
            'city',
            'town',
            'province',
            'image'
        )