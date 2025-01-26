from django.contrib import admin
from .models import User
# Register the custom User model with the Django admin site
admin.site.register(User)
