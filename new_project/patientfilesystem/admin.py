from django.contrib import admin
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest

admin.site.register(Patient)
admin.site.register(HealthHistory)
admin.site.register(Treatment)
admin.site.register(Diagnosis)
admin.site.register(ScreeningTest)