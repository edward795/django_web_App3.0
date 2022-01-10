"""
WSGI config for app_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys 

from django.core.wsgi import get_wsgi_application

path = '/home/admin/django_project/app_web'
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_web.settings')

application = get_wsgi_application() 

