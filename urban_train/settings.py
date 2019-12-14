import os
import environ

BASE_DIR = environ.Path(__file__) - 2
ROOT_DIR = environ.Path(__file__) - 2

env = environ.Env()
env.read_env(ROOT_DIR('.envs/.local/.env'))

SECRET_KEY = env('DJANGO_SECRET_KEY', default='apjfqc9e8r-9eq3r3u49u4399r43-@#%^^^')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'bn8&xf8i916nuk=ma8wsi420yhmu%kly4@5i#d-ir!@&+0b+az'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["gastosluxu.com.br"])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # lib
    'widget_tweaks',
    # Third-party
    'cruds_adminlte',
    # apps
    'core',
    'website'
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

ROOT_URLCONF = 'urban_train.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'urban_train.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///promosys'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
# DATABASES['default']['conn_max_age'] = 600


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static/')

# auth
LOGIN_URL = '/entrar/'
AUTH_USER_MODEL = 'core.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'core.backends.ModelBackend',
)
