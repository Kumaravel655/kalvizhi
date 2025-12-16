import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project directory to Python path
sys.path.append('/var/www/kalvizhi/backend')
sys.path.append('/var/www/kalvizhi/venv/lib/python3.x/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kalvizhi_project.settings_production')
application = get_wsgi_application()