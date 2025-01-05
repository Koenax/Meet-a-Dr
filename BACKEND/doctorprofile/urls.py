from django.urls import path
from . import api

urlpatterns = [
    path('', api.doctor_list, name='doctorprofile_list'),  # This matches the root of api/doctors/
]
