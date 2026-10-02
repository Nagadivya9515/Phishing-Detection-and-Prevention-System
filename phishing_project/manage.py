#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Instructs Django to look into your configuration folder for its runtime variables
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phishing_project.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # Takes the commands you pass via terminal (like runserver) and executes them
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
