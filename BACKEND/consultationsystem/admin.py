from django.contrib import admin
from .models import CallConsultation

@admin.register(CallConsultation)
class CallConsultationAdmin(admin.ModelAdmin):
       list_display = ('doctor', 'patient', 'meeting_id', 'call_type', 'status', 'created_at')
