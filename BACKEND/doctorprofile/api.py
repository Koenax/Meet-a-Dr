from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import DoctorProfile
from .serializers import DoctorProfileListSerializer, DoctorProfileDetailsSerializer
from .forms import DoctorProfileForm


# API view for listing all doctor profiles
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def doctor_list(request):
    """
    Get a list of all doctor/practice profiles
    """
    doctors = DoctorProfile.objects.all()
    serializer = DoctorProfileListSerializer(doctors, many=True)
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
    doctorprofile = DoctorProfile.objects.get(pk=pk)
    serializer = DoctorProfileDetailsSerializer(doctorprofile, many=False)
    return JsonResponse(serializer.data)

# API view for creating a new doctor profile
@api_view(['POST', 'FILES'])
def create_doctorprofile(request):
    # Handling file uploads
    form = DoctorProfileForm(request.POST, request.FILES)

    if form.is_valid():
        doctorprofile = form.save(commit=False)
        doctorprofile.user = request.user
        doctorprofile.save()

        return JsonResponse({'success': True})
    else:
        print('Error:', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)
