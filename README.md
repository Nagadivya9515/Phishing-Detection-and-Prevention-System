# Phishing Detection and Prevention System

An automated, intelligent security web pipeline designed to analyze incoming email assets and website URL structures in real-time. Built using **Python**, **Django**, and **Scikit-Learn**, this application extracts semantic features and processes them through machine learning classifiers to accurately identify malicious patterns and protect users from deceptive attacks.

## 🚀 Key Features

* **Real-Time Analysis Input Engine**: Simple web portal accepting suspected text payloads or domains for instant evaluation.
* **Intelligent Feature Extraction**: Automated parser evaluating string metadata, including URL character length variations, abnormal `@` token insertions, domain mutations, and IP-based hosting configurations.
* **Machine Learning Pipeline**: Clean integration architecture prepared for loading serialized predictive models to calculate probabilistic classification risks.
* **Interactive Telemetry Dashboard**: Dark-themed analytics console visualizing data ingestion counts, historical log models, and performance metrics (Accuracy, Precision, Recall, F1-Scores).

## 🛠️ Tech Stack & Dependencies

* **Backend Framework**: Django (Python)
* **Machine Learning Core**: Scikit-Learn, Pandas, NumPy
* **Frontend Design**: HTML5, CSS3 Component Layouts

## ⚙️ Quick Start Installation

1. **Clone the repository and navigate into the workspace root folder:**
   ```bash
   cd phishing_project
   ```

2. **Install the required system dependency packages:**
   ```bash
   pip install django scikit-learn pandas numpy requests
   ```

3. **Initialize the local relational database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Launch the local network development hosting server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application modules via your local web browser terminal:**
   * Main Checker Interface: `http://127.0.0`
   * Performance Dashboard: `http://127.0.0dashboard/`
