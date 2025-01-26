from django.contrib import admin
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest


admin.site.register(Patient)
admin.site.register(HealthHistory)
admin.site.register(Treatment) # Treatment: Records treatment details for patients.
admin.site.register(Diagnosis) #  Diagnosis: Contains diagnosis information for patients.
admin.site.register(ScreeningTest)
