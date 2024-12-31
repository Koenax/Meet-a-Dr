from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Patient, HealthHistory, Treatment, Diagnosis, ScreeningTest
from .serializers import PatientSerializer, HealthHistorySerializer, TreatmentSerializer, DiagnosisSerializer, ScreeningTestSerializer
from .forms import PatientForm

# API view for retrieving a specific patient profile
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def patient_details(request, pk):
    """
    Get a specific patient's details by ID
    """
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
    """
    Get all health history records for a specific patient
    """
    histories = HealthHistory.objects.filter(patient__id=patient_id)
    serializer = HealthHistorySerializer(histories, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a health history record
@api_view(['POST'])
def create_health_history(request):
    """
    Create a new health history record
    """
    serializer = HealthHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# API view for listing all treatments for a patient
@api_view(['GET'])
def treatment_list(request, patient_id):
    """
    Get all treatments for a specific patient
    """
    treatments = Treatment.objects.filter(patient__id=patient_id)
    serializer = TreatmentSerializer(treatments, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a treatment
@api_view(['POST'])
def create_treatment(request):
    """
    Create a new treatment for a patient
    """
    serializer = TreatmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# API view for listing all diagnoses for a patient
@api_view(['GET'])
def diagnosis_list(request, patient_id):
    """
    Get all diagnoses for a specific patient
    """
    diagnoses = Diagnosis.objects.filter(patient__id=patient_id)
    serializer = DiagnosisSerializer(diagnoses, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a diagnosis
@api_view(['POST'])
def create_diagnosis(request):
    """
    Create a new diagnosis for a patient
    """
    serializer = DiagnosisSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)

# API view for listing all tests for a patient
@api_view(['GET'])
def test_list(request, patient_id):
    """
    Get all tests for a specific patient
    """
    tests = ScreeningTest.objects.filter(patient__id=patient_id)
    serializer = ScreeningTestSerializer(tests, many=True)
    return JsonResponse({'data': serializer.data})

# API view for creating a test
@api_view(['POST'])
def create_test(request):
    """
    Create a new test for a patient
    """
    serializer = ScreeningTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True, 'data': serializer.data})
    else:
        return JsonResponse({'errors': serializer.errors}, status=400)
