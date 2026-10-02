# detector/models.py
from django.db import models

class ScanLog(models.Model):
    """
    Database schema table to record and archive every processed 
    security analysis event for real-time telemetry metrics tracking.
    """
    # 1. Target URL column: Stores the evaluated web string or email asset source
    target_url = models.CharField(max_length=2083) # 2083 is the standard maximum URL length allowed by browsers
    
    # 2. Risk Classification column: Holds the machine learning prediction output
    risk_classification = models.CharField(max_length=50) # Expected strings: "Safe", "Phishing", "Suspicious"
    
    # 3. Timestamp column: Automatically logs the date and time of ingestion
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Human-readable representation string for the Django Admin dashboard portal panel.
        """
        return f"{self.target_url} -> {self.risk_classification}"
