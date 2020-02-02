from .base import *


DEBUG = False

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
    # '/var/www/static/',
]

print('Loaded production environment.....!')