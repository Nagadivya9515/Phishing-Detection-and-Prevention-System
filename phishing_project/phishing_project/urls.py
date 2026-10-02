"""
phishing_project URL Configuration
The master switchboard mapping network paths to internal functional application routers.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Django Administrative Control Room System
    path('admin/', admin.site.urls),
    
    # 2. Application Feature Integration Sub-Router 
    # Emptied quotes '' represents the homepage. Any traffic coming onto the root domain 
    # gets instantly handed over to your custom 'detector.urls' engine file.
    path('', include('detector.urls')),
]
