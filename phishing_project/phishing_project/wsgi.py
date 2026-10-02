"""
WSGI config for phishing_project.

It exposes the WSGI callable as a module-level variable named ``application``.
This script serves as the structural gateway hook that handles pipeline requests 
when deploying this app onto a live production server.
"""

import os

from django.core.wsgi import get_wsgi_application

# 1. Map the location environmental pointers to our control room
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phishing_project.settings')

# 2. Build the server interface loop callable application context
application = get_wsgi_application()
