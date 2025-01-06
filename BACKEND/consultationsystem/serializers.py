from rest_framework import serializers
from .models import BookingConsultation

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
            'timeslot',
            'consultation_type',
            'status',
        )