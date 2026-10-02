# detector/urls.py
from django.urls import path
from . import views

# Set an app name namespace to easily reference these routes across your templates
app_name = 'detector'

urlpatterns = [
    # 1. Main Portal Page (URL / Email Input Checker View)
    # Accessible via: http://127.0.0
    path('', views.url_checker, name='url_checker'),
    
    # 2. Performance Analytics Dashboard View
    # Accessible via: http://127.0.0dashboard/
    path('dashboard/', views.dashboard, name='dashboard'),
]
