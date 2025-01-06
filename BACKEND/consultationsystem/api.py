from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from doctorprofile.models import DoctorProfile
from .models import BookingConsultation
from .serializers import BookingConsultationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def create_booking(request):
    """
    Create a new booking for a client.
    """
    try:
        patient = request.user.patient
    except AttributeError:
        return JsonResponse({'error': 'User is not associated with a patient'}, status=400)

    doctor_id = request.data.get('doctor') 
    appointment_time = request.data.get('appointment_time')
    
    if not doctor_id or not appointment_time:
        return JsonResponse({'error': 'Doctor and appointment_time are required fields'}, status=400)

    try:
        doctor = DoctorProfile.objects.get(id=doctor_id)
    except DoctorProfile.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)

    # Create the booking
    booking = BookingConsultation.objects.create(
        doctor=doctor,
        patient=patient,
        appointment_time=appointment_time
    )

    serializer = BookingConsultationSerializer(booking)
    return JsonResponse({'data': serializer.data}, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient_bookings(request):
    """
    Get all bookings for the logged-in patient (client).
    """
    try:
        patient = request.user.patient
    except AttributeError:
        return JsonResponse({'error': 'User is not associated with a patient'}, status=400)
    
    bookings = BookingConsultation.objects.filter(patient=patient)
    serializer = BookingConsultationSerializer(bookings, many=True)
    return JsonResponse({'data': serializer.data}, status=200)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def confirm_booking(request, pk):
    """
    Confirm or cancel a booking
    """
    try:
        booking = BookingConsultation.objects.get(pk=pk)
        status = request.data.get('status')
        
        if status not in ['confirmed', 'cancelled']:
            return JsonResponse({'error': 'Invalid status'}, status=400)

        booking.status = status
        booking.save()
        booking.send_notification()
        return JsonResponse({'message': f'Booking status updated to {booking.status}'}, status=200)
    except BookingConsultation.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctor_bookings(request):
    """
    Get all bookings for the logged-in doctor.
    """
    try:
        doctor = request.user.doctorprofile
    except AttributeError:
        return JsonResponse({'error': 'User is not associated with a doctor'}, status=400)

    bookings = BookingConsultation.objects.filter(doctor=doctor)
    serializer = BookingConsultationSerializer(bookings, many=True)
    return JsonResponse({'data': serializer.data}, status=200)
