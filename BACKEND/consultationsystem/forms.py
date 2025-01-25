from django import forms
from .models import CallConsultation

class CallForm(forms.ModelForm):
    class Meta:
           model = CallConsultation
           fields = ['doctor', 'patient', 'appointment', 'call_type']
