from .base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Setting for sending emails: Contact form.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'test@example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_j6TE8wziTY7GfstmdTOr1YgB')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_ILy21dWXXOZiX89YcOA3iCku')

SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://discover-thailand.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'thailandbusiness.sandbox@yahoo.com'
