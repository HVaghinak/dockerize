import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'megg_yej86ln@xao^+)it4e&amp;ueu#!4tl9p1h%2sjr7ey0)m25f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  
TEMPLATE_DEBUG = True  
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'dockerize',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # required by Django 1.9
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin'

)

TEMPLATES = [{

}]

MIDDLEWARE_CLASSES = (  
)

ROOT_URLCONF = 'dockerize.urls'

WSGI_APPLICATION = 'dockerize.wsgi.application'

# Localization ant timezone settings

TIME_ZONE = 'UTC'  
USE_TZ = True

CELERY_ENABLE_UTC = True  
CELERY_TIMEZONE = "UTC"

LANGUAGE_CODE = 'en-us'  
USE_I18N = True  
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

DATABASES = {  
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Redis

REDIS_PORT = 6379  
REDIS_DB = 0  
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'redis')


# Celery configuration

# configure queues, currently we have only one
CELERY_DEFAULT_QUEUE = 'default'

# Sensible settings for celery
CELERY_ALWAYS_EAGER = False  
CELERY_ACKS_LATE = True  
CELERY_TASK_PUBLISH_RETRY = True  
CELERY_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
CELERY_IGNORE_RESULT = False  
CELERY_SEND_TASK_ERROR_EMAILS = False  
CELERY_TASK_RESULT_EXPIRES = 600

# Set redis as celery result backend
CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)  
CELERY_REDIS_MAX_CONNECTIONS = 1

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"  
CELERY_ACCEPT_CONTENT = ['application/json']

CELERYD_HIJACK_ROOT_LOGGER = False  
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000

