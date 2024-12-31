from rest_framework import serializers
from .models import DoctorProfile, Category
from manageusers.serializers import UserDetailsSerializer

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = (
            'id',
            'practice_name',
            'rating',
            'image_url'
            )
        

class DoctorProfileDetailsSerializer(serializers.ModelSerializer):
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
            'price',
            )
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_category']