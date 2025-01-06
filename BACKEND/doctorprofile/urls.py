from django.urls import path
from . import api

urlpatterns = [
    path('', api.doctor_list, name='doctor_profile_list'),
]