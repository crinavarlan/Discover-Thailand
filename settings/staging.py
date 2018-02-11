from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_j6TE8wziTY7GfstmdTOr1YgB')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_ILy21dWXXOZiX89YcOA3iCku')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://discover-thailand.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'thailandbusiness.sandbox@yahoo.com'

SITE_URL = 'https://discover-thailand.herokuapp.com'
ALLOWED_HOSTS.append('discover-thailand.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}