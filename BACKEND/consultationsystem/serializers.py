from rest_framework import serializers
from .models import BookingConsultation, CallConsultation

class BookingConsultationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model..
    """
    class Meta:
        model = BookingConsultation
        fields = (
            'id',
            'patient',
            'doctor',
            'appointment_time',
            'consultation_type',
            'status',
        )

class CallConsultationSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and retrieving video/voice call sessions.
    """
    class Meta:
        model = CallConsultation
        fields = (
            'id',
            'doctor',
            'patient',
            'appointment',
            'meeting_id',
            'call_type',
            'status',
        )