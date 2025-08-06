"""
WSGI config for webpersonal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# 📌 Ruta al directorio que contiene settings.py
path = '/home/MiguelMO/webpersonal/webpersonal'

# ✅ Añade la ruta si no está ya presente
if path not in sys.path:
    sys.path.append(path)

# 🧭 Indica a Django dónde están los settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')

# 🚀 Crea la aplicación WSGI
application = get_wsgi_application()
