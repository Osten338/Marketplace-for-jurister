"""
WSGI config for marketplace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/runner/Marketplace-for-jurister/venv/lib/python3.10/site-packages')
import traceback
from django.core.wsgi import get_wsgi_application

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
    application = get_wsgi_application()
except Exception:
    print(traceback.format_exc())
    raise


