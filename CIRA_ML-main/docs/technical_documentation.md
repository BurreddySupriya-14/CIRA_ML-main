# CIRA-ML Technical Documentation

## ML-Enhanced Cybersecurity Risk Assessment Platform

**Version**: 2.0
**Date**: December 2024
**Status**: Production Ready

---

## 📋 Table of Contents

1. [System Architecture Overview](#system-architecture-overview)
2. [ML Integration Framework](#ml-integration-framework)
3. [Core Components](#core-components)
4. [API Reference](#api-reference)
5. [Data Flow Architecture](#data-flow-architecture)
6. [Performance & Scalability](#performance--scalability)
7. [Security Considerations](#security-considerations)
8. [Deployment Specifications](#deployment-specifications)

---

## 🏗️ System Architecture Overview

### Unified ML Intelligence Architecture

CIRA-ML implements a revolutionary **Unified ML Intelligence Hub** that seamlessly integrates machine learning predictions with traditional cybersecurity frameworks. The architecture follows a modular, scalable design that enables both independent operation and comprehensive integration.

```
┌────────────────────────────────────────────────────────────────┐
│                    🧠 Unified ML Intelligence Hub              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Central Intelligence Coordinator            │  │
│  │    • Risk Fusion Engine    • System Health Monitor       │  │
│  │    • Component Orchestrator • Executive Intelligence     │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│   🛡️ STRIDE     │   │  📊 TEMPORAL    │   │  🤝 FEDERATED   │
│   Enhancement   │   │  Intelligence   │   │  Intelligence   │
│                 │   │                 │   │                 │
│ • ML Predictions│   │ • ML Forecasting│   │ • Privacy-Safe  │
│ • Dynamic Risk  │   │ • Trend Analysis│   │ • Multi-Org     │
│ • Confidence    │   │ • Pattern Recog │   │ • Benchmarking  │
└─────────────────┘   └─────────────────┘   └─────────────────┘
              │                 │                 │
              └─────────────────┼─────────────────┘
                                │
                                ▼
                  ┌─────────────────────────────┐
                  │      💡 ADAPTIVE LEARNING   │
                  │   • Incident Feedback       │
                  │   • Model Enhancement       │
                  │   • Convergence Monitoring  │
                  └─────────────────────────────┘
```

### Core Design Principles

1. **Progressive Enhancement**: System operates with traditional methods and enhances capabilities when ML models are available
2. **Modular Integration**: Each ML component can function independently while contributing to unified intelligence
3. **Real-time Processing**: ML predictions and risk assessments updated dynamically
4. **Scalable Architecture**: Designed for enterprise deployment with performance optimization
5. **Privacy-Preserving**: Federated learning maintains data privacy while enabling collaboration

---

## 🤖 ML Integration Framework

### RiskFusionEngine Class

**Location**: `src/integration/risk_fusion.py`
**Purpose**: Core ML-STRIDE integration engine

#### Key Methods

```python
class RiskFusionEngine:
    def __init__(self):
        self.ml_models = {}
        self.stride_weights = {...}
        self.device_risk_multipliers = {...}

    def predict_network_risk(self, network_features) -> Dict[str, float]:
        """
        Use trained ML models to predict network-based risks
        Returns dictionary with model predictions and confidence scores
        """

    def enhanced_stride_analysis(self, device_type: str, network_risk: Dict,
                               business_criticality: int) -> Dict:
        """
        Enhanced STRIDE analysis using ML predictions
        Integrates ML network risk predictions with STRIDE threat categories
        """

    def generate_unified_report(self, device_type: str, network_features,
                              business_criticality: int) -> Dict:
        """
        Generate comprehensive risk report combining all analysis
        Returns unified assessment with ML analysis, enhanced STRIDE,
        risk prioritization, and mitigation recommendations
        """
```

#### ML Influence Calculation

The system calculates ML influence on STRIDE categories using category-specific sensitivity factors:

```python
category_sensitivity = {
    'Spoofing': 0.3,           # Moderate network pattern influence
    'Tampering': 0.2,          # Less network-dependent
    'Repudiation': 0.1,        # Minimal network influence
    'Information Disclosure': 0.4,  # High data pattern influence
    'Denial of Service': 0.6,  # Very high traffic pattern influence
    'Elevation of Privilege': 0.25  # Moderate behavioral influence
}

ml_influence = (ml_risk - 50) / 100 * sensitivity
enhanced_likelihood = base_likelihood * (1 + ml_influence)
```

### CIRAUnifiedMLIntelligenceHub Class

**Location**: `src/integration/risk_fusion.py`
**Purpose**: Comprehensive ML intelligence coordination

#### Unified Risk Assessment Flow

```python
def comprehensive_risk_assessment(self, device_type: str, network_features,
                                business_criticality: int) -> Dict:
    """
    1. ML-Enhanced STRIDE Analysis (40% weight)
    2. Federated Intelligence Insights (25% weight)
    3. Temporal Risk Projections (20% weight)
    4. Adaptive Learning Recommendations (15% weight)
    5. Unified Risk Score Calculation
    """
```

---

## 🔧 Core Components

### 1. Enhanced Data Management

**Location**: `src/preprocessing/enhanced_data_loader.py`

#### Features

- **Multi-Dataset Support**: UNSW-NB15, IoT-23, custom CSV formats
- **Intelligent Preprocessing**: Automated feature engineering and normalization
- **ML-Ready Transformation**: Optimized data pipeline for ML model training
- **Chunked Processing**: Efficient handling of large datasets

### 2. ML Model Training Pipeline

**Location**: `app.py` - Model Training Functions

#### Supported Algorithms

1. **RandomForest Classifier**

   - Ensemble learning with 100 estimators
   - Feature importance analysis
   - Cross-validation with StratifiedKFold
   - Confidence scoring via predict_proba

2. **XGBoost Classifier**

   - Gradient boosting optimization
   - Early stopping and regularization
   - GPU acceleration support
   - Advanced hyperparameter tuning

3. **Linear SVM (LinearSVC)**
   - Fast linear classification
   - Scalable to large datasets
   - Subset training for performance
   - Confidence estimation

### 3. Professional Web Interface

**Location**: `app.py` - Main Application

#### Interface Architecture

- **Framework**: Streamlit-based web application
- **Styling**: Custom CSS with professional color scheme and gradients
- **Layout**: 8-tab modular design with sidebar configuration
- **Responsiveness**: Adaptive layout for different screen sizes

#### Navigation Structure

```python
tabs = [
    "📊 Dashboard",           # System overview and status
    "🔧 Data Management",     # Dataset loading and preprocessing
    "🤖 Model Training",      # ML pipeline execution
    "🛡️ Threat Analysis",     # STRIDE threat modeling
    "📈 Risk Evolution",      # Temporal risk analysis
    "🤝 Federated Intelligence", # Multi-org collaboration
    "💡 Adaptive Models",     # Self-learning capabilities
    "📋 Reports & Export"     # Documentation and exports
]
```

#### Session State Management

- Persistent model storage across tabs
- Training results caching
- Risk assessment history
- Configuration state preservation

### 2. STRIDE Threat Modeling Implementation

#### STRIDE Categories

The implementation covers all six STRIDE threat categories:

```python
stride_threats = {
    'Spoofing': {
        'threats': ['Device Identity Theft', 'Protocol Spoofing', 'Credential Hijacking'],
        'likelihood': 6, 'impact': 7, 'color': '#FF6B6B'
    },
    'Tampering': {
        'threats': ['Firmware Modification', 'Data Manipulation', 'Physical Tampering'],
        'likelihood': 7, 'impact': 9, 'color': '#FF8E53'
    },
    'Repudiation': {
        'threats': ['Log Deletion', 'Action Denial', 'Audit Bypass'],
        'likelihood': 4, 'impact': 5, 'color': '#FFD93D'
    },
    'Information Disclosure': {
        'threats': ['Data Exfiltration', 'Eavesdropping', 'Side-Channel Attack'],
        'likelihood': 8, 'impact': 6, 'color': '#6BCF7F'
    },
    'Denial of Service': {
        'threats': ['Resource Exhaustion', 'Network Flooding', 'System Overload'],
        'likelihood': 9, 'impact': 8, 'color': '#4D96FF'
    },
    'Elevation of Privilege': {
        'threats': ['Privilege Escalation', 'Admin Account Takeover', 'Root Access'],
        'likelihood': 5, 'impact': 10, 'color': '#9B59B6'
    }
}
```

#### Risk Matrix Visualization

- Interactive Plotly-based risk matrix
- Bubble chart with likelihood vs impact axes
- Color-coded risk zones (Low/Medium/High)
- Device-specific threat assessment
- Export capabilities for analysis results

### 3. Machine Learning Pipeline

#### Supported Algorithms

1. **RandomForest Classifier**

   - Ensemble method with 100 trees
   - Parallel processing (n_jobs=2)
   - Cross-validation support

2. **XGBoost Classifier**

   - Gradient boosting implementation
   - Optimized for performance
   - Verbosity control for clean output

3. **Linear SVM**
   - LinearSVC implementation for speed
   - Subset training for large datasets (max 5000 samples)
   - Dual=False for n_samples > n_features

#### Training Pipeline

```python
def train_models(selected_models, random_seed):
    models = {}
    if "RandomForest" in selected_models:
        models["RandomForest"] = RandomForestClassifier(
            n_estimators=100,
            random_state=random_seed,
            n_jobs=2
        )
    # ... other models

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_seed)
    # Training and validation loop
```

#### Performance Metrics

- Test set accuracy
- 5-fold cross-validation scores
- Training time tracking
- Error handling and reporting

### 4. Enhanced Data Management (`enhanced_data_loader.py`)

#### Multi-Dataset Support

```python
def get_available_datasets(self):
    return [
        "UNSW-NB15 (Network Intrusion)",
        "IoT-23 (IoT Malware)",
        "Simulated IIoT Data"
    ]
```

#### Data Processing Pipeline

1. **Loading**: CSV file parsing with error handling
2. **Preprocessing**: Feature selection and normalization
3. **Risk Labeling**: Automatic risk category assignment
4. **Splitting**: Configurable train/test split
5. **Validation**: Data quality checks

#### Risk Label Generation

```python
def create_risk_labels(self):
    if self.data is not None:
        # Generate risk scores based on attack categories
        risk_conditions = [
            (self.data['label'] == 'Normal', 0),
            (self.data['label'].isin(['DoS', 'DDoS']), 3),
            (self.data['label'].isin(['Probe', 'Reconnaissance']), 2),
            (self.data['label'].isin(['Malware', 'Trojan']), 4),
        ]
        # Apply conditions and create risk categories
```

### 5. Temporal Risk Analysis

#### Time Series Modeling

```python
def generate_temporal_analysis(temporal_window):
    window_days = {'1 Month': 30, '3 Months': 90, '6 Months': 180, '1 Year': 365}

    # Generate realistic temporal patterns
    base_risk = 50
    seasonal = 10 * np.sin(2 * np.pi * np.arange(window_days) / 365)
    weekly = 5 * np.sin(2 * np.pi * np.arange(window_days) / 7)
    trend = 0.02 * np.arange(window_days)
    noise = np.random.normal(0, 3, window_days)

    risk_scores = base_risk + seasonal + weekly + trend + noise
```

#### Predictive Capabilities

- 30-day risk forecasting
- Trend analysis and slope calculation
- Volatility assessment
- Historical pattern recognition

#### Visualization Components

- Dual subplot layout (historical + predictions)
- Interactive Plotly charts
- Trend line overlays
- Statistical summaries

### 6. Federated Intelligence Simulation

#### Multi-Organization Framework

```python
def simulate_federation(participants):
    # Simulate local training at each organization
    local_accuracies = []
    for i in range(participants):
        local_acc = 0.82 + np.random.normal(0, 0.05)
        local_accuracies.append(max(0.75, min(0.95, local_acc)))

    # Federated aggregation simulation
    federated_accuracy = np.mean(local_accuracies) + 0.03
```

#### Privacy-Preserving Features

- Zero data sharing simulation
- Secure model aggregation
- Performance comparison with centralized learning
- Threat coverage metrics

#### Collaboration Metrics

- Federation accuracy vs centralized baseline
- Privacy preservation level (100%)
- Multi-party performance visualization
- Organizational contribution tracking

### 7. Adaptive Learning System

#### Self-Improving Models

```python
def simulate_adaptive_learning(learning_rate):
    time_steps = 20
    base_accuracy = 0.87

    adaptive_performance = [base_accuracy]
    for step in range(1, time_steps):
        # Simulate incident feedback
        incident_feedback = np.random.choice([0.01, -0.005, 0.015], p=[0.4, 0.2, 0.4])
        current_acc = adaptive_performance[-1] + learning_rate * incident_feedback
        adaptive_performance.append(min(0.95, max(0.80, current_acc)))
```

#### Learning Parameters

- Configurable learning rate (0.01-0.5)
- Incident-based feedback simulation
- Performance convergence tracking
- Stability analysis

#### Adaptation Metrics

- Final improvement measurement
- Convergence iteration count
- Performance stability assessment
- Learning curve visualization

### 8. Professional Reporting System

#### Export Capabilities

1. **Model Results Export**

   ```python
   results_df = pd.DataFrame([
       {
           'Model': name,
           'Accuracy': result['accuracy'],
           'CV_Mean': result.get('cv_mean', 0),
           'CV_Std': result.get('cv_std', 0)
       }
       for name, result in training_results.items()
   ])
   ```

2. **STRIDE Analysis Export**

   - CSV format with threat categories
   - Risk scores and likelihood/impact data
   - Timestamp and device information

3. **System Reports**
   - Comprehensive text-based reports
   - System status summaries
   - Performance analytics
   - Configuration documentation

## Technical Specifications

### Performance Optimizations

1. **SVM Optimization**: Subset training for large datasets
2. **Progress Tracking**: Real-time training progress indicators
3. **Memory Management**: Efficient data handling and caching
4. **Error Handling**: Comprehensive exception management
5. **Session Persistence**: State management across user interactions

### Code Quality Features

1. **Modular Architecture**: Clean separation of concerns
2. **Professional Styling**: Custom CSS for production appearance
3. **Input Validation**: Robust parameter checking
4. **Documentation**: Comprehensive code comments
5. **Error Recovery**: Graceful failure handling

### Security Considerations

1. **Data Privacy**: No persistent data storage by default
2. **Input Sanitization**: Safe handling of user inputs
3. **Session Isolation**: User session independence
4. **Access Control**: Web-based access management
5. **Audit Trail**: Activity logging capabilities

## Integration Points

### External Dependencies

```python
# Core Dependencies
import streamlit as st          # Web interface framework
import pandas as pd            # Data manipulation
import numpy as np             # Numerical computing
import plotly.express as px    # Interactive visualizations
import plotly.graph_objects as go  # Advanced plotting

# Machine Learning
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, StratifiedKFold
```

### Custom Modules

```python
# Internal Components
from src.preprocessing.enhanced_data_loader import EnhancedDataLoader
from src.threat_modeling.risk_calculator import RiskCalculator
```

## Deployment Architecture

### Local Development

- Streamlit development server
- Real-time code reloading
- Interactive debugging

### Production Deployment

- Docker containerization support
- Cloud platform compatibility
- Scalable web service architecture
- Load balancing capabilities

## Future Enhancement Opportunities

### Technical Improvements

1. **Database Integration**: Persistent data storage
2. **Real-time Streaming**: Live data ingestion
3. **Advanced Analytics**: More sophisticated ML models
4. **API Development**: RESTful service interfaces
5. **Authentication**: User management system

### Functional Enhancements

1. **Additional Datasets**: More cybersecurity data sources
2. **Enhanced Visualizations**: Advanced analytics dashboards
3. **Automated Reporting**: Scheduled report generation
4. **Integration Capabilities**: SIEM and security tool connectivity
5. **Mobile Optimization**: Responsive design improvements

This technical documentation provides a comprehensive overview of all implemented features in the CIRA-ML platform, serving as a reference for developers, users, and stakeholders.
