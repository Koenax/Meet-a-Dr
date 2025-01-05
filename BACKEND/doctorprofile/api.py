from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import DoctorProfile
from .serializers import DoctorProfileListSerializer


# API view for listing all doctor profiles
@api_view(['GET'])
@authentication_classes([])  # If no authentication required
@permission_classes([])  # If no permission required
def doctor_list(request):
    """
    Get a list of all doctor/practice profiles
    """
    doctors = DoctorProfile.objects.all()
    serializer = DoctorProfileListSerializer(doctors, many=True)
    return JsonResponse({
        'data': serializer.data
    })