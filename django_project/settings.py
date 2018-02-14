# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django_project.credentials as credentials
import netifaces
import raven

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
def ip_addresses():
    ip_list = ['localhost', 'buakpsi.com', 'www.buakpsi.com']
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

# Discover our IP address
ALLOWED_HOSTS = ip_addresses()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = credentials.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL=True

# Application definition

INSTALLED_APPS = (
    'brothers',
    'buakpsi',
    'eye2eye',
    'nccg',
    'rush',
    'ubru', # vinay put this here



    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'buakpsi',
        'USER': credentials.DB['USER'],
        'PASSWORD': credentials.DB['PASSWORD'],
        'HOST': credentials.DB['HOST'],
        'PORT': credentials.DB['PORT'],
    }
}

# Emails
EMAIL_HOST = credentials.EMAIL['HOST']
EMAIL_HOST_USER = credentials.EMAIL['HOST_USER']
EMAIL_HOST_PASSWORD = credentials.EMAIL['HOST_PASSWORD']
EMAIL_PORT = credentials.EMAIL['PORT']
EMAIL_USE_TLS = credentials.EMAIL['USE_TLS']


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/django/django_project/django_project/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

RAVEN_CONFIG = {
    'dsn': 'https://bf26be97ba1a4d70888557d2ec1ce02b:05407d23dc8446f0a0c5a6e3a1613a07@sentry.io/282062',
}