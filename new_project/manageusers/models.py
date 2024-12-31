from django.db import models

#models.py

import uuid
from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.core.validators import RegexValidator


class CustomUserManager(UserManager):
    """
    Manager for the User model that provides helper methods 
    for creating regular users and superusers.
    """

    def _create_user(self, email, name, password, **extra_fields):
        """
        Helper method to create and save a user with the provided email, 
        name, password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        """
        Create and return a regular user with an email, name, and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        """
        Create and return a superuser with admin privileges.
        """
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model that extends AbstractBaseUser and PermissionsMixin.
     - UUIDField used as the primary key for better security and scalability.
     - Email field used as the unique identifier for the user.
     - Avatar field for the user to upload their profile images.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='uploads/avatars/', null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        validators=[RegexValidator(r'^[0-9]{10}$', 'Enter a valid phone number')]
    )

    # Flags for user differentiation
    is_medium = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    
    # Flag to indicate if the user account is active
    is_active = models.BooleanField(default=True)
   
    # Flag to indicate if the user is a superuser/staff member.
    # Superusers have full access to the system and administrative privileges.
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
  
    #  DateTime field
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    # Groups and permissions for role-based access control
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def avatar_url(self):
        """
        Returns the URL of the user's avatar image, if available.
        """
        if self.avatar:
            return f'{settings.WEBSITE_URL}{self.avatar.url}'
        return ''
