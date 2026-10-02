# detector/admin.py
from django.contrib import admin
from .models import ScanLog

@admin.register(ScanLog)
class ScanLogAdmin(admin.ModelAdmin):
    """
    Customizes the visual presentation layout grid inside the Django 
    Administrative portal control board.
    """
    # 1. Columns displayed on the database directory overview grid index screen
    list_display = ('target_url', 'risk_classification', 'scanned_at')
    
    # 2. Creates interactive sidebar navigation filters to parse logs instantly
    list_filter = ('risk_classification', 'scanned_at')
    
    # 3. Embeds a functional search input bar targeting specific string matches
    search_fields = ('target_url',)
    
    # 4. Sets the default descending timeline sorting view order parameter
    ordering = ('-scanned_at',)
