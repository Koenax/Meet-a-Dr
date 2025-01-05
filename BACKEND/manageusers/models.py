import uuid
from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

class CustomUserManager(UserManager):
    """
    Manager for the User model with methods for creating users and superusers.
    """

    def _create_user(self, name, email, password, **extra_fields):
        """
        Helper method that performs the actual creation of a User object with the provided details.
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
        Create and return a regular user with an email, username, and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        """
        Create and return a superuser with an email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model with additional fields like email and profile.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='uploads/avatars', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(blank=True, null=True)

    # Add groups and user_permissions fields
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

    USERNAME_FIELD = 'email'  # Use email as the username field
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]  # Fields required for creating a user

    def avatar_url(self):
        if self.avatar:
            return f'{settings.WEBSITE_URL}{self.avatar.url}'
        else:
            return ''
