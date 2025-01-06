from django.urls import path
from . import api

urlpatterns = [
    path('', api.doctor_list, name='doctor_profile_list'),
    path('create/', api.create_doctorprofile, name='doctor_profile_create'),
    path('<uuid:pk>/', api.doctorprofile_details, name='doctor_profile_details'),
]