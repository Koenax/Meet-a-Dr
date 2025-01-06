from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Doctor, Appointment
from .serializers import UserSerializer, DoctorSerializer, AppointmentSerializer

# ViewSets for CRUD operations
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# Views for Communication Features
class VideoCallView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        doctor_id = request.data.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        # Logic to generate video call link
        video_call_link = f"https://example.com/video/{doctor_id}"
        return Response({"message": "Video call link generated", "link": video_call_link}, status=status.HTTP_200_OK)

class VoiceCallView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        doctor_id = request.data.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        # Logic to initiate a voice call
        voice_call_status = "Initiated"
        return Response({"message": "Voice call initiated", "status": voice_call_status}, status=status.HTTP_200_OK)

class TextCommunicationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        doctor_id = request.data.get("doctor_id")
        message = request.data.get("message")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        # Logic to send a text message
        message_status = "Sent"
        return Response({"message": "Message sent", "status": message_status}, status=status.HTTP_200_OK)

