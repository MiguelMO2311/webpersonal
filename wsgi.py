"""
WSGI config for webpersonal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Indica a Django dónde está el archivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Crea la aplicación WSGI
application = get_wsgi_application()