from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest
from .serializers import PatientSerializer, HealthHistorySerializer, TreatmentSerializer, DiagnosisSerializer, ScreeningTestSerializer
from .forms import PatientForm


# API view for listing patient profile
@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return JsonResponse(serializer.data)

# API view for retrieving a specific patient profile
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def patient_details(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient, many=False)
        return JsonResponse(serializer.data)
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)

# API view for creating a new patient
@api_view(['POST'])
def create_patient(request):
    form = PatientForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    return JsonResponse({'errors': form.errors}, status=400)

# API view for listing all health history records for a patient
@api_view(['GET'])
def health_history_list(request, patient_id):
    histories = HealthHistory.objects.filter(patient__id=patient_id)
    serializer = HealthHistorySerializer(histories, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a health history record
@api_view(['POST'])
def create_health_history(request, patient_id):
    """
    Create a new health history record
    """
    data = request.data
    data['patient'] = patient_id  # Ensure patient is included in the data
    serializer = HealthHistorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# API view for listing all treatments for a patient
@api_view(['GET'])
def treatment_list(request, patient_id):
    treatments = Treatment.objects.filter(patient__id=patient_id)
    serializer = TreatmentSerializer(treatments, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a treatment
@api_view(['POST'])
def create_treatment(request, patient_id):
    """
    Create a new treatment for a patient
    """
    data = request.data
    data['patient'] = patient_id  # Ensure patient is included in the data
    serializer = TreatmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# API view for listing all diagnoses for a patient
@api_view(['GET'])
def diagnosis_list(request, patient_id):
    diagnoses = Diagnosis.objects.filter(patient__id=patient_id)
    serializer = DiagnosisSerializer(diagnoses, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a diagnosis
@api_view(['POST'])
def create_diagnosis(request, patient_id):
    """
    Create a new diagnosis for a patient
    """
    data = request.data
    data['patient'] = patient_id
    serializer = DiagnosisSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# API view for listing all tests for a patient
@api_view(['GET'])
def test_list(request, patient_id):
    tests = ScreeningTest.objects.filter(patient__id=patient_id)
    serializer = ScreeningTestSerializer(tests, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a test
@api_view(['POST'])
def create_test(request, patient_id):
    """
    Create a new test for a patient
    """
    data = request.data
    data['patient'] = patient_id
    serializer = ScreeningTestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)
