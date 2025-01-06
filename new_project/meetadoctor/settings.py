import os
from datetime import timedelta
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SET THE CUSTOM USER MODEL
AUTH_USER_MODEL = 'manageusers.User'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS specifies the host/domain names that this Django site can serve.
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=lambda v: v.split(','))

# SITE_ID specifies the ID of the current site in the database. This is used in Django sites framework.
SITE_ID = config('SITE_ID', default=1, cast=int)

# WEBSITE_URL is the base URL of the website, typically used for constructing links.
WEBSITE_URL = config('WEBSITE_URL', default='https://localhost:8000')

# SIMPLE_JWT is the configuration for the Simple JWT authentication package.
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=config('ACCESS_TOKEN_LIFETIME', default=60, cast=int)),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=config('REFRESH_TOKEN_LIFETIME', default=7, cast=int)),
    "ROTATE_FRESH_TOKEN": config('ROTATE_FRESH_TOKEN', default=False, cast=bool),
    "BLACKLIST_AFTER_ROTATION": config('BLACKLIST_AFTER_ROTATION', default=False, cast=bool),
    "UPDATE_LAST_LOGIN": config('UPDATE_LAST_LOGIN', default=True, cast=bool),
    "SIGNING_KEY": config('JWT_SIGNING_KEY'),
    "ALGORITHM": config('JWT_ALGORITHM', default='HS512'),
}

# ACCOUNT_EMAIL_REQUIRED determines whether an email address is required to create an account.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
USER_MODEL_USERNAME_FIELD = 'email'

# Django Rest Framework (DRF) related settings for API configurations.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# CORS (Cross-Origin Resource Sharing) settings for allowing cross-origin requests.
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=lambda v: v.split(','))

REST_AUTH = {
    "USE_JWT": config('USE_JWT', default=True, cast=bool),
    "JWT_AUTH_HTTPONLY": config('JWT_AUTH_HTTPONLY', default=False, cast=bool),
}

# Application definition

INSTALLED_APPS = [
    'manageusers',
    'doctorprofile',
    'patientfilesystem',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
    'cities_light',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meetadoctor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meetadoctor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'meetadoctor_db',
        'USER': 'postgres',
        'PASSWORD': 'Keamo',
        'HOST': 'db',
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': 10,  # Optional: Increase timeout for connection attempts
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = config('STATIC_URL', default='static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'