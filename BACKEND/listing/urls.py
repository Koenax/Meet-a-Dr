from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api
from .views import (
    UserViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    VideoCallView,
    VoiceCallView,
    TextCommunicationView,
)

# Router setup for CRUD operations
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

# endpoint 
urlpatterns = [
    path('', api.doctor_list, name='doctor-list'),  # Existing endpoint
    path('crud/', include(router.urls)),  # Add CRUD endpoints under '/crud/'
    path('video-call/', VideoCallView.as_view(), name='video-call'),
    path('voice-call/', VoiceCallView.as_view(), name='voice-call'),
    path('text/', TextCommunicationView.as_view(), name='text-communication'),
