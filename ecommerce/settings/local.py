from .base import *

DEBUG=True

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
