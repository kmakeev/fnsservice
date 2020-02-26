"""
WSGI config for fnsservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.update(DJANGO_SETTINGS_MODULE='fnsservice.settings')

application = get_wsgi_application()
