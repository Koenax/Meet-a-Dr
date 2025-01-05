"""
URL configuration for meetadoctor project.

The `urlpatterns` list routes URLs to views.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctors', include('doctorprofile.urls')),
]