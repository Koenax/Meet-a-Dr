from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer, DoctorProfileDetailsSerializer
from .forms import DoctorProfileForm

# API view for listing all doctor profiles
@api_view(['GET'])
@authentication_classes([])  # If no authentication required
@permission_classes([])  # If no permission required
def doctor_list(request):
    """
    Get a list of all doctor profiles
    """
    doctors = DoctorProfile.objects.all()
    serializer = DoctorProfileSerializer(doctors, many=True)
    return JsonResponse({
        'data': serializer.data
    })

# API view for displaying a specific doctor profile details
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def doctorprofile_details(request, pk):
    """
    Get a specific doctor profile by ID
    """
    try:
        doctorprofile = DoctorProfile.objects.get(pk=pk)
        serializer = DoctorProfileDetailsSerializer(doctorprofile, many=False)
        return JsonResponse(serializer.data)
    except DoctorProfile.DoesNotExist:
        return JsonResponse({'error': 'Doctor profile not found'}, status=404)

# API view for creating a new doctor profile
@api_view(['POST'])
def create_doctorprofile(request):
    # Handling file uploads
    form = DoctorProfileForm(request.POST, request.FILES)

    if form.is_valid():
        doctorprofile = form.save(commit=False)
        doctorprofile.user = request.user  # Assuming user is authenticated
        doctorprofile.save()  # Save the doctor profile

        return JsonResponse({'success': True})
    else:
        print('Error:', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)