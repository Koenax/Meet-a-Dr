from django.urls import path
from . import api

# URL patterns for the booking-related API endpoints in the Django Consultation System
urlpatterns = [
    path('', api.create_booking, name='create_booking'),
    path('bookings/<uuid:pk>/confirm/', api.confirm_booking, name='confirm_booking'),
    
    path('bookings/patient/', api.get_patient_bookings, name='get_patient_bookings'),
    path('bookings/doctor/', api.get_doctor_bookings, name='get_doctor_bookings'),

    path('bookings/<uuid:booking_id>/initiate-call/', api.initiate_call, name='initiate_call'),
]
