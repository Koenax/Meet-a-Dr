from django.urls import path
from . import api  # Assuming api refers to function-based views

urlpatterns = [
    # Patient Endpoints
    path('', api.patient_list, name='patient_list'),  # List all patients
    path('patients/create/', api.create_patient, name='create_patient'),  # Create a new patient
    path('patients/<uuid:pk>/', api.patient_details, name='patient_details'),  # Retrieve a specific patient profile
    
    # Health History Endpoints
    path('patients/<uuid:patient_id>/health_histories/', api.health_history_list, name='health_history_list'),  # List health histories for a specific patient
    path('patients/<uuid:patient_id>/health_histories/create/', api.create_health_history, name='create_health_history'),  # Create health history for a patient
    
    # Treatment Endpoints
    path('patients/<uuid:patient_id>/treatments/', api.treatment_list, name='treatment_list'),  # List treatments for a specific patient
    path('patients/<uuid:patient_id>/treatments/create/', api.create_treatment, name='create_treatment'),  # Create treatment for a patient
    
    # Diagnosis Endpoints
    path('patients/<uuid:patient_id>/diagnoses/', api.diagnosis_list, name='diagnosis_list'),  # List diagnoses for a specific patient
    path('patients/<uuid:patient_id>/diagnoses/create/', api.create_diagnosis, name='create_diagnosis'),  # Create diagnosis for a patient
    
    # Screening Test Endpoints
    path('patients/<uuid:patient_id>/screening_tests/', api.test_list, name='screening_test_list'),  # List screening tests for a specific patient
    path('patients/<uuid:patient_id>/screening_tests/create/', api.create_test, name='create_test'),  # Create screening test for a patient
]
