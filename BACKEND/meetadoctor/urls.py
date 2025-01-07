"""
URL configuration for meetadoctor project.

The `urlpatterns` list routes URLs to views.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home_view(request):
    return HttpResponse(" WELCOME TO MEET A DOCTOR")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctors/', include('doctorprofile.urls')),
    path('api/auth/', include('manageusers.urls')),
    path('api/patient/', include('patientfilesystem.urls')),
    path('api/booking/', include('consultationsystem.urls')),
    path('', home_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)