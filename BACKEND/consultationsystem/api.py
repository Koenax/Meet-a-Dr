from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BookingConsultation
from .serializers import BookingConsultationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def get_patient_bookings(request):
    """
    Get all bookings for the logged-in patient (client).
    """
    try:
        # Get the patient associated with the authenticated user
        patient = request.user.patient
    except Patient.DoesNotExist:
        # Handle cases where the user is not associated with a Patient
        return Response({'error': 'User is not associated with a patient'}, status=400)
    
    bookings = BookingConsultation.objects.filter(patient=patient)
    serializer = BookingConsultationSerializer(bookings, many=True)
    return Response({'data': serializer.data})

    
