from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50)
    
class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='patient_appointments')
    doctor = models.ForeignKey(Doctor, related_name='doctor_appointments')
    date = models.DateField()
    time = models.TimeField()
