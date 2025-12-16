# Django Backend Apache Deployment Guide

## 1. Install Required Packages
```bash
sudo apt update
sudo apt install apache2 python3-pip python3-venv libapache2-mod-wsgi-py3
```

## 2. Setup Project Directory
```bash
sudo mkdir -p /var/www/kalvizhi
sudo chown -R $USER:$USER /var/www/kalvizhi
cd /var/www/kalvizhi
```

## 3. Upload and Setup Django Project
```bash
# Upload your backend folder to /var/www/kalvizhi/
# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Configure Django Settings
Create `backend/kalvizhi/settings_production.py`:
```python
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com', 'your-server-ip']

# Database (update with your production database)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/www/kalvizhi/backend/db.sqlite3',
    }
}

# Static files
STATIC_ROOT = '/var/www/kalvizhi/backend/static/'
STATIC_URL = '/static/'

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
    "http://your-frontend-domain.com",
]
```

## 5. Create WSGI Configuration
Create `/var/www/kalvizhi/backend/wsgi.py`:
```python
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project directory to Python path
sys.path.append('/var/www/kalvizhi/backend')
sys.path.append('/var/www/kalvizhi/venv/lib/python3.x/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kalvizhi.settings_production')
application = get_wsgi_application()
```

## 6. Apache Virtual Host Configuration
Create `/etc/apache2/sites-available/kalvizhi.conf`:
```apache
<VirtualHost *:80>
    ServerName your-domain.com
    ServerAlias www.your-domain.com
    DocumentRoot /var/www/kalvizhi/backend
    
    WSGIDaemonProcess kalvizhi python-path=/var/www/kalvizhi/backend python-home=/var/www/kalvizhi/venv
    WSGIProcessGroup kalvizhi
    WSGIScriptAlias / /var/www/kalvizhi/backend/wsgi.py
    
    <Directory /var/www/kalvizhi/backend>
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
    
    Alias /static /var/www/kalvizhi/backend/static
    <Directory /var/www/kalvizhi/backend/static>
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/kalvizhi_error.log
    CustomLog ${APACHE_LOG_DIR}/kalvizhi_access.log combined
</VirtualHost>
```

## 7. Enable Site and Restart Apache
```bash
sudo a2ensite kalvizhi.conf
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
```

## 8. Setup Database and Static Files
```bash
cd /var/www/kalvizhi/backend
source ../venv/bin/activate
python manage.py migrate --settings=kalvizhi.settings_production
python manage.py collectstatic --settings=kalvizhi.settings_production
python manage.py createsuperuser --settings=kalvizhi.settings_production
```

## 9. Set Permissions
```bash
sudo chown -R www-data:www-data /var/www/kalvizhi
sudo chmod -R 755 /var/www/kalvizhi
sudo chmod 664 /var/www/kalvizhi/backend/db.sqlite3
```

## 10. SSL Setup (Optional but Recommended)
```bash
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d your-domain.com -d www.your-domain.com
```

## API Endpoints Available:
- `https://your-domain.com/api/users/`
- `https://your-domain.com/api/courses/`
- `https://your-domain.com/api/applications/`
- `https://your-domain.com/admin/`

## Troubleshooting:
```bash
# Check Apache error logs
sudo tail -f /var/log/apache2/kalvizhi_error.log

# Restart Apache
sudo systemctl restart apache2

# Check Apache status
sudo systemctl status apache2
```