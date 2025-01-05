from rest_framework import serializers
from .models import DoctorProfile


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