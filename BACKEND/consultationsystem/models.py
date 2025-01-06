from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from manageusers.models import User
from doctorprofile.models import DoctorProfile
from patientfilesystem.models import Patient

class BookingConsultation(models.Model):
    """
    Represents a booking for a doctor's consultation.
    """
    CONSULTATION_CHOICES = [
        ('in_person', 'In Person'),
        ('voice', 'Voice Call'),
        ('video', 'Video Call'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_CHOICES)
    status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')])
    created_at = models.DateTimeField(auto_now_add=True)

    def send_notification(self):
        """
        Sends email notifications to the patient and doctor confirming or updating
        the status of the booking.
        """

        # Subject and message content for notification
        subject = f"Booking Confirmation for {self.patient.first_name} with {self.doctor.first_name}"
        message = f"Your consultation on {self.timeslot} is scheduled as {self.consultation_type}.\n\nBooking Status: {self.status}"

        # Sending email to patient
        send_mail(subject, message, 'noreply@meetadoctor.com', [self.patient.user.email])

        # Sending email to doctor
        send_mail(subject, message, 'noreply@meetadoctor.com', [self.doctor.user.email])