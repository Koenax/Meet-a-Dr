from django import forms
from .models import DoctorProfile

# Doctor's profile form
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
