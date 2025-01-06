from rest_framework import serializers
from users.models import User, DoctorProfile, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['id', 'name', 'specialty']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time']
