from rest_framework import serializers
from .models import DoctorProfile
from manageusers.serializers import UserDetailsSerializer

class DoctorProfileListSerializer(serializers.ModelSerializer):
    """
    summarized view of a doctor's profile for listing or search results
    """
    class Meta:
        model = DoctorProfile
        fields = (
            'id',
            'practice_name',
            'category',
            'rating',
            'image_url'
            )
        

class DoctorProfileDetailsSerializer(serializers.ModelSerializer):
     """
     detailed view of the doctors profile
     """
     user = UserDetailsSerializer(read_only=True, many=False)
     class Meta:
        model = DoctorProfile
        fields = (
            'id',
            'practice_name',
            'rating',
            'bio',
            'services_offered',
            'category',
            'consultation_fee',
            )
