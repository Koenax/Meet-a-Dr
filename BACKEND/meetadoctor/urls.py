"""
URL configuration for meetadoctor project.

The `urlpatterns` list routes URLs to views. 
"""
# In your project/urls.py (main urls.py)
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Optional: A basic view for the root URL
def home(request):
    return HttpResponse('Welcome to the Meet a Doctor app!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctors/', include('doctorprofile.urls')),
    path('', home, name='home'),  # This will handle the root URL
]
