"""
URL configuration for meetadoctor project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
    path('api/patientfile/', include('patientfilesystem.urls')),
    path('', home_view),
]