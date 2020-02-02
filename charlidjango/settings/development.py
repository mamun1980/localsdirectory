from .base import *

DEBUG = True

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


STATIC_ROOT = (
    os.path.join(BASE_DIR, 'static'),
)


print('Loaded development environment.....!')