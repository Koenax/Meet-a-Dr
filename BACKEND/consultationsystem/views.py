from django.shortcuts import render, get_object_or_404
from .models import CallConsultation

def start_call(request, appointment_id):
       # Logic to start a call
       pass

def join_call(request, meeting_id):
       call = get_object_or_404(CallConsultation, meeting_id=meeting_id)
       # Logic to join a call
       pass



