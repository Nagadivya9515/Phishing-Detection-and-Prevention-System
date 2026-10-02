# detector/apps.py
from django.apps import AppConfig

class DetectorConfig(AppConfig):
    """
    Main application registry configuration class for the threat detector module.
    """
    # 1. Sets the default primary auto-incrementing field type for database model rows
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 2. Defines the exact module path name string Django maps internally 
    name = 'detector'
