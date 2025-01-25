from django.urls import path
from . import api
from . import views
 
urlpatterns = [
    path('', api.create_booking, name='create_booking'),
    path('bookings/<uuid:pk>/confirm/', api.confirm_booking, name='confirm_booking'),
    
    path('bookings/patient/', api.get_patient_bookings, name='get_patient_bookings'),
    path('bookings/doctor/', api.get_doctor_bookings, name='get_doctor_bookings'),

    path('bookings/<uuid:booking_id>/initiate-call/', api.initiate_call, name='initiate_call'),
    
    path('start-call/<int:appointment_id>/', views.start_call, name='start_call'),
       path('join-call/<str:meeting_id>/', views.join_call, name='join_call'),

]
