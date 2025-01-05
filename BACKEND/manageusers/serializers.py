from rest_framework import serializers
from manageusers.models import User

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """
    class Meta:
        model = User
        fields =(
            'id',
            'name',
            'avatar_url'
        )

class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new user.
    handles password validation and creation
    """
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type':'password'})

    class Meta:
        model = User
        fields = ['id', 'name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data('name', None),
            password=validated_data['password'],
        )
