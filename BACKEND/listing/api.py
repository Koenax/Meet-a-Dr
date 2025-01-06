from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer

# API view for listing all doctor profiles
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def doctor_list(request):
    """
    Get a list of all doctor profiles
    """
    doctors = DoctorProfile.objects.all()
    serializer = DoctorProfileSerializer(doctors, many=True)
    
    return JsonResponse({
        'data':serializer.data
        })