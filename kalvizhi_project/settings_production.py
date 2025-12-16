
 
from .settings import *

# Production settings
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com', 'your-server-ip']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/www/kalvizhi/backend/db.sqlite3',
    }
}

# Static files
STATIC_ROOT = '/var/www/kalvizhi/backend/static/'
STATIC_URL = '/static/'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
    "http://your-frontend-domain.com",
]

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True