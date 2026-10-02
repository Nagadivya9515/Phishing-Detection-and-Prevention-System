# ml_engine/train_model.py
import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def build_and_serialize_model():
    """
    Simulates security training raw datasets, trains a supervised 
    RandomForest classifier machine learning framework model, 
    and serializes the pipeline using pickle.
    """
    print("🤖 Starting Phishing Detection ML Pipeline Execution...")

    # 1. Synthesize Labeled Security Data Records
    # Feature 1: long_url (1 = suspicious length, 0 = safe short length)
    # Feature 2: has_at_symbol (1 = present decoy redirection, 0 = missing)
    # Feature 3: is_ip_address (1 = raw numeric routing destination, 0 = standard domain)
    # Target Class: label (1 = Phishing Vector, 0 = Safe Website)
    mock_security_data = {
        'long_url':'',
        'has_at_symbol':'',
        'is_ip_address':'',
        'label': [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0]
    }

    # Transform python dictionary collections into structured DataFrames
    df = pd.DataFrame(mock_security_data)
    
    # Save simulated dataset to disk for project file complete integrity
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_csv_path = os.path.join(current_dir, 'dataset.csv')
    df.to_csv(dataset_csv_path, index=False)
    print(f"📊 Dataset successfully generated and cached at: {dataset_csv_path}")

    # 2. Separate Independent Input Vectors from Classification Labels
    X = df[['long_url', 'has_at_symbol', 'is_ip_address']]
    y = df['label']

    # Divide vectors into Train versus Evaluation Validation pools
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Instantiate and Train Classifier Structure
    print("⚙️ Training RandomForest predictive decision classifier tree model arrays...")
    model_classifier = RandomForestClassifier(n_estimators=50, random_state=42)
    model_classifier.fit(X_train, y_train)

    # 4. Pipeline Performance Assessment Telemetry Analytics
    predictions = model_classifier.predict(X_test)
    
    print("\n📈 Calculated Project Metric Performance Telemetry Matrix:")
    print(f" * Model Accuracy Score: {accuracy_score(y_test, predictions) * 100:.1f}%")
    print(f" * Precision Validity:    {precision_score(y_test, predictions) * 100:.1f}%")
    print(f" * Recall Sensitivity:   {recall_score(y_test, predictions) * 100:.1f}%")
    print(f" * Comprehensive F1-Score: {f1_score(y_test, predictions) * 100:.1f}%")

    # 5. Output Model Serialization Using Pickle Storage
    target_pickle_path = os.path.join(current_dir, 'phishing_model.pkl')
    with open(target_pickle_path, 'wb') as output_file:
        pickle.dump(model_classifier, output_file)
        
    print(f"\n💾 Serialized classifier artifact successfully exported to: {target_pickle_path}")
    print("✅ Pipeline ready for live integration inside web execution views.")

if __name__ == '__main__':
    build_and_serialize_model()
