from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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
    except AttributeError:
        # Handle cases where the user is not associated with a Patient
        return JsonResponse({'error': 'User is not associated with a patient'}, status=400)
    
    bookings = BookingConsultation.objects.filter(patient=patient)
    serializer = BookingConsultationSerializer(bookings, many=True)
    return JsonResponse({'data': serializer.data}, status=200)

@api_view(['PATCH'])
def confirm_booking(request, pk):
    """
    Confirm or cancel a booking
    """
    try:
        booking = BookingConsultation.objects.get(pk=pk)
        booking.status = request.data.get('status', booking.status)
        booking.save()
        booking.send_notification()
        return JsonResponse({'message': f'Booking status updated to {booking.status}'}, status=200)
    except BookingConsultation.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)
