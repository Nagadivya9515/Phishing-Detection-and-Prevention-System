# detector/views.py
from django.shortcuts import render
import os
import re
import pickle
from pathlib import Path
from .models import ScanLog

# Automatically locate the root project folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'ml_engine' / 'phishing_model.pkl'

def extract_url_features(url_string):
    """
    Extracts structural feature metrics from raw web input strings.
    Returns an ordered numerical list [long_url, has_at, is_ip] matching 
    the shape expected by your Scikit-Learn classifier vector pipeline.
    """
    # Feature 1: Check length variations
    long_url = 1 if len(url_string) > 54 else 0
    
    # Feature 2: Check for abnormal user redirection character '@'
    has_at_symbol = 1 if '@' in url_string else 0
    
    # Feature 3: Check if domain structure mimics raw numeric IP address hosting
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    is_ip_address = 1 if ip_pattern.search(url_string) else 0

    return [long_url, has_at_symbol, is_ip_address]

def url_checker(request):
    """
    Manages client-side queries, reads the input string, passes it through the 
    predictive ML model, and saves the transaction history logs into the local database.
    """
    context = {
        'classification': None,
        'scanned_url': None
    }
    
    if request.method == "POST":
        user_url = request.POST.get('url_input', '').strip()
        context['scanned_url'] = user_url
        
        # 1. Pipeline Feature Extraction
        numerical_features = extract_url_features(user_url)
        
        # 2. Predictive ML Model Execution Block
        # Attempts to load your serialized pkl model. If you haven't trained it yet, 
        # it falls back to a clean fallback rule-engine so your site stays operational.
        if os.path.exists(MODEL_PATH):
            try:
                with open(MODEL_PATH, 'rb') as model_file:
                    trained_model = pickle.load(model_file)
                
                # Model expects an array structure: array matching shape [[feature_1, feature_2, ...]]
                prediction = trained_model.predict([numerical_features])[0]
                classification_result = "Phishing" if prediction == 1 else "Safe"
            except Exception:
                classification_result = "Suspicious (Model Execution Failure)"
        else:
            # Clean Fallback Heuristic Rule-Engine
            if numerical_features[0] == 1 or numerical_features[1] == 1:
                classification_result = "Phishing"
            else:
                classification_result = "Safe"
                
        context['classification'] = classification_result
        
        # 3. Structural Log Generation & Database Commits
        # Saves the scan session directly into SQLite for the analytics dashboard to reference.
        ScanLog.objects.create(
            target_url=user_url,
            risk_classification=classification_result
        )
            
    return render(request, 'detector/index.html', context)

def dashboard(request):
    """
    Calculates live metric counters from your SQLite logs to render data 
    visualization streams onto your analytical monitoring interface.
    """
    # Fetch historical logging transactions from the database
    all_logs = ScanLog.objects.all().order_by('-scanned_at')
    
    # Calculate dataset aggregate telemetry summaries
    total_count = all_logs.count()
    phishing_count = all_logs.filter(risk_classification="Phishing").count()
    safe_count = all_logs.filter(risk_classification="Safe").count()
    
    # Bundle data arrays to display on dashboard screens
    context = {
        'total_scans': total_count,
        'phishing_vectors': phishing_count,
        'safe_vectors': safe_count,
        'recent_logs': all_logs[:10]  # Display the 10 most recent logs
    }
    return render(request, 'detector/dashboard.html', context)
