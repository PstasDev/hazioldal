from pathlib import Path
import local_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# helyi szerverbeállítások

SECRET_KEY = local_settings.SECRET_KEY

DEBUG = local_settings.DEBUG

ALLOWED_HOSTS = ['127.0.0.1', '157.230.123.12']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'APP.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'PROJEKT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'PROJEKT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if local_settings.MELYIK=='otthon':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif local_settings.MELYIK=='DigitalOcean': 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': local_settings.DB_NAME,
            'USER': local_settings.DB_USER,
            'PASSWORD': local_settings.DB_PASSWORD,
            'HOST': local_settings.DB_HOST,
            'PORT': '',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTHENTICATION #
LOGIN_REDIRECT_URL = '/'


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# INNEN szedegeti össze azokat a statikus fájlokat, amelyek nem tartoznak egyetlen apphoz sem:
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# IDE fogja collectelni a collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'  
#régebbi django-hoz: 
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ITT fogja észlelni a böngésző
STATIC_URL = '/static/'

# itt a whitenoise alkalmazása
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = local_settings.EMAIL_HOST
EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD
EMAIL_PORT = local_settings.EMAIL_PORT
EMAIL_USE_TLS = local_settings.EMAIL_USE_TLS
DEFAULT_FROM_EMAIL = local_settings.DEFAULT_FROM_EMAIL
