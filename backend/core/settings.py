from pathlib import Path
from decouple import config
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY",default="ajdsndaskdn3123!@#8123ajakj") # developing mode
# SECRET_KEY = config("SECRET_KEY") # production mode

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG",cast=bool,default="True") # developing mode
# DEBUG = config("DEBUG",cast=bool) # production mode

ALLOWED_HOSTS = config("ALLOWED_HOSTS",cast=lambda v:[s.strip() for s in v.split(",")],default="*")


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog_module',
    'account_module',
    'rest_framework',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/' #this is for load static in templates==> {% static '<directory/file.format>' %}
STATIC_ROOT=BASE_DIR / "static"
# This is the directory that use for production mode and when you run collectstatic command,
# All the static files that are in static directories collect in this directory.

# This is for all the directory that set in django settings and load all the static files in developing mode
STATICFILES_DIRS = [ BASE_DIR / 'static_files' ] # developing mode and doesnt need for production
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # developing mode


#media url is for load and server medias in site and templates
MEDIA_URL='/media/'

#media root is for uploading medias from user and site.it needs to add urls in base urls project
MEDIA_ROOT= BASE_DIR / 'media'
# MEDIA_ROOT= os.path.join(BASE_DIR, 'media')



# Production static and media configs
# STATIC_URL = "/static/"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static') # production mode
# STATIC_ROOT=BASE_DIR.parent / "static"
# This is the directory that use for production mode and when you run collectstatic command,
# All the static files that are in static directories collect in this directory.

# MEDIA_URL="/media_files/"
# MEDIA_ROOT=BASE_DIR.parent / "media_files"



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Extra Configs
AUTH_USER_MODEL='account_module.User'

# LOGIN_URL = ''


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # remember that basic and session authentications set default for authentication and if we dont set them django still uses them.
        # for example if we send request in postman with basic authentication for endpoint that need permission something like isAuthenticated we can send username and password with basic authentication. 
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}