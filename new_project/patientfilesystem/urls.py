from django.urls import path
from . import api

urlpatterns = [
    path('patients/', api.patient_details, name='patient_details'),
    path('patients/create/', api.create_patient, name='create_patient'),

    path('health_histories/', api.health_history_list, name='health_history_list'),
    path('health_histories/create/', api.create_health_history, name='create_health_history'),

    path('treatments/', api.treatment_list, name='treatment_list'),
    path('treatments/create/', api.create_treatment, name='create_treatment'),

    path('diagnoses/', api.diagnosis_list, name='diagnosis_list'),
    path('diagnoses/create/', api.create_diagnosis, name='create_diagnosis'),

    path('screening_tests/', api.test_list, name='screening_test_list'),
    path('screening_tests/create/', api.create_test, name='create_test'),
]