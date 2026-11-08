# CIRA-ML Usage Guide
## Complete ML-Enhanced Cybersecurity Risk Assessment Workflow

**Version**: 2.0
**Target Audience**: Security Analysts, SOC Teams, Industrial IoT Specialists
**Difficulty Level**: Beginner to Advanced

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Dashboard Overview](#dashboard-overview)
3. [ML Model Training Workflow](#ml-model-training-workflow)
4. [ML-Enhanced STRIDE Analysis](#ml-enhanced-stride-analysis)
5. [Predictive Risk Evolution](#predictive-risk-evolution)
6. [Federated Intelligence](#federated-intelligence)
7. [Adaptive Learning System](#adaptive-learning-system)
8. [Advanced Analytics & Reporting](#advanced-analytics--reporting)
9. [Troubleshooting & FAQ](#troubleshooting--faq)

---

## 🚀 Getting Started

### Initial System Setup

#### **Prerequisites Installation**

**For Windows Users:**
```cmd
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**For Linux/macOS Users:**
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### **Launch CIRA-ML Application**

**Windows Command Prompt:**
```cmd
# Activate virtual environment
venv\Scripts\activate
streamlit run app.py
```

**Windows PowerShell:**
```powershell
# Activate virtual environment
venv\Scripts\Activate.ps1
streamlit run app.py
```

**Linux/macOS Terminal:**
```bash
# Activate virtual environment
source venv/bin/activate
streamlit run app.py
```

**Access the Application:**
- Navigate to `http://localhost:8501` in your web browser
- If port 8501 is busy, Streamlit will automatically use the next available port

#### **System Status Check**
- Observe the main dashboard for system health indicators
- Check if the **Unified ML Intelligence Hub** shows "Train ML models to activate"
- Note that all advanced ML features require trained models

#### **First Steps Workflow**
```
Data Management → Model Training → ML-Enhanced Analysis
```

---

## 📊 Dashboard Overview

### Unified ML Intelligence Hub

The dashboard provides real-time monitoring of your ML-enhanced cybersecurity intelligence system.

#### **When No Models Are Trained**
```
🔧 Train ML models to activate the Unified Intelligence Hub

The Unified ML Intelligence Hub integrates:
• ML-Enhanced STRIDE Analysis - Dynamic threat modeling with ML predictions
• Federated Intelligence - Collaborative learning across organizations
• Temporal Risk Analysis - Predictive risk forecasting with ML
• Adaptive Learning - Self-improving models with incident feedback
```

#### **When Models Are Active**
- **🤖 System Health**: Overall ML component health status
- **📊 ML Components**: Active component count (X/5)
- **🎯 Unified Risk**: Current risk level with score
- **📈 ML Models**: Number of trained models

#### **Component Status Indicators**
- 🛡️ **STRIDE Enhanced**: Green if ML-STRIDE integration active
- 🤝 **Federated Ready**: Green if federated learning available
- 📈 **Temporal Active**: Green if predictive analysis enabled
- 💡 **Adaptive Learning**: Green if incident feedback system active
- 🧠 **Unified Intelligence**: Green if all components integrated

### Quick Actions

- **🚀 Generate ML Intelligence Summary**: One-click comprehensive risk assessment
- **📊 Performance Overview**: Model accuracy and training results
- **📈 Risk Summary**: Current threat assessment status

---

## 🤖 ML Model Training Workflow

### Phase 1: Data Preparation

#### **Step 1: Navigate to Data Management Tab**
```
📋 Data Management Tab → Dataset Selection
```

#### **Step 2: Configure Dataset**
- **Dataset Options**:
  - `UNSW-NB15 (Network Intrusion)` - 39 features, 9 attack categories
  - `IoT-23 (IoT Malware)` - Specialized IoT threat data
  - `Simulated IIoT Data` - Industrial IoT simulation

- **Configuration Parameters**:
  - **Test Split**: 10-50% (default: 20%)
  - **Random Seed**: For reproducible results (default: 42)

#### **Step 3: Load Dataset**
```
Click: 📊 Load Dataset
```

**Expected Output**:
```
✅ Data loaded successfully!
Dataset: UNSW-NB15 with 257,673 samples and 39 features
✅ Train set: 206,138 samples | Test set: 51,535 samples
✅ Risk labels generated: Low (X%), Medium (Y%), High (Z%)
```

### Phase 2: Model Training

#### **Step 1: Navigate to Model Training Tab**
```
🤖 Model Training Tab → Algorithm Selection
```

#### **Step 2: Configure ML Pipeline**
- **Model Selection** (Recommended: Select all)
  - ☑️ **RandomForest**: Robust ensemble learning
  - ☑️ **XGBoost**: High-performance gradient boosting
  - ☑️ **SVM**: Fast linear classification

- **Advanced Configuration**:
  - **Cross-Validation**: 5-fold (automatic)
  - **Performance Metrics**: Accuracy, Precision, Recall, F1-Score
  - **Progress Tracking**: Real-time training status

#### **Step 3: Execute Training**
```
Click: 🚀 Train Selected Models
```

**Training Progress Indicators**:
```
🚀 Training Progress
Overall Progress: [████████████████████] 100%

Processing 1/3: RandomForest
Individual Model Progress: [████████████] 75%
🔄 Cross-validating... RandomForest

Training Stats:
Current Model: RandomForest
Training Samples: 206,138
Test Samples: 51,535
Features: 39
```

**Expected Results**:
```
✅ Training completed successfully!

Model Performance:
• RandomForest: 0.9033 accuracy (CV: 0.8987 ± 0.0123)
• XGBoost: 0.8999 accuracy (CV: 0.8945 ± 0.0156)
• SVM: 0.8876 accuracy (CV: 0.8821 ± 0.0134)

🧠 ML Intelligence Hub: ACTIVATED
```

### Phase 3: Persistent Model Storage

#### **Step 1: Smart Save System**
After successful training, CIRA-ML provides intelligent model persistence:

**📁 Model Management Section**:
```
💾 Save Newly Trained Models
💾 Save Models  ← GREEN, ACTIVE BUTTON

📂 Load Saved Models
📭 No saved models available (if first time)

🗑️ Current Session
✅ 3 models loaded
🔥 Freshly trained (can save)
```

#### **Step 2: Save Trained Models**
```
Click: 💾 Save Models
```

**Expected Output**:
```
✅ Models saved successfully!
Path: saved_models/cira_models_20241224_143052.pkl

📁 Model Management Section Updates:
💾 Save Newly Trained Models
📂 These models were loaded from disk
(already saved - no need to save again)

🗑️ Current Session
✅ 3 models loaded
📂 Loaded from disk
```

#### **Step 3: Future Sessions (Auto-Loading)**
When you restart the application:

**Auto-Load Behavior**:
```
🚀 Auto-loaded 3 models from 2024-12-24 14:30:52 (toast notification)

📂 Load Saved Models
2024-12-24 14:30:52 (3 models)  ← Available in dropdown

🗑️ Current Session
✅ 3 models loaded
📂 Loaded from disk
```

#### **Benefits of Persistent Storage**:
- **Train Once, Use Forever**: No need to retrain models each session
- **Instant Demo Ready**: Models load automatically for immediate use
- **Duplicate Prevention**: Smart save logic prevents accidental duplicates
- **Version Control**: Multiple timestamped model sets available
- **Team Collaboration**: Share saved model files between team members

---

## 🛡️ ML-Enhanced STRIDE Analysis

### Understanding ML-Enhanced STRIDE

Traditional STRIDE analysis uses static likelihood values. ML-Enhanced STRIDE dynamically adjusts threat likelihood based on real-time ML predictions.

#### **Enhancement Mechanism**:
```python
# Traditional STRIDE
risk_score = likelihood * impact / 10

# ML-Enhanced STRIDE
ml_influence = calculate_ml_influence(network_predictions)
enhanced_likelihood = base_likelihood * (1 + ml_influence)
enhanced_risk_score = enhanced_likelihood * enhanced_impact / 10
```

### Running ML-Enhanced STRIDE Analysis

#### **Step 1: Navigate to Threat Analysis Tab**
```
🛡️ Threat Analysis Tab → STRIDE Assessment
```

#### **Step 2: Configure Analysis**
- **Device Type Selection**:
  - `PLC Controller` - Industrial process control (Risk Multiplier: 1.2x)
  - `HMI Interface` - Human-machine interface (Risk Multiplier: 1.0x)
  - `Industrial Sensors` - Sensor networks (Risk Multiplier: 0.8x)
  - `Network Gateway` - Network infrastructure (Risk Multiplier: 1.4x)
  - `SCADA System` - Supervisory control (Risk Multiplier: 1.5x)
  - `Industrial Camera` - Visual monitoring (Risk Multiplier: 0.6x)

- **Business Criticality**: 1-10 scale (impacts risk scoring)

#### **Step 3: Execute Analysis**
```
Click: 🔍 Run STRIDE Analysis
```

**ML-Enhanced Analysis Progress**:
```
🔍 ML-Enhanced STRIDE Analysis Progress

🔄 Initializing ML-enhanced analysis...
✅ ML models detected - Enhanced analysis enabled

🔄 Generating network features for ML analysis...
🔄 Running ML network risk prediction...
🔄 Integrating ML insights with STRIDE framework...
✅ ML-enhanced STRIDE analysis completed!

Final ML-Enhanced Results:
- STRIDE Categories: 6
- ML-Enhanced Categories: 4/6
- High Risk Categories: 2
- ML Average Risk: 67.3/100
- Overall Risk Score: 7.2/10
```

### Interpreting ML-Enhanced Results

#### **STRIDE Matrix Visualization**
- **🤖 Enhanced Categories**: Green markers with robot emoji
- **📊 Traditional Categories**: Purple markers
- **Hover Information**:
  ```
  Denial of Service 🤖
  Likelihood: 9.4/10 (ML Enhanced)
  Impact: 8.0/10
  Risk Score: 7.52
  ML Influence: +0.156
  ML Enhanced: Yes
  ```

#### **ML Intelligence Summary**
```
🤖 ML Intelligence Summary:
- ML Models Used: 3
- ML Average Risk: 67.3/100
- ML-Enhanced Categories: 4/6
- Overall Integration Score: 7.2/10

🎯 ML Model Predictions:
- RandomForest: 65.2/100 (89.3% confidence)
- XGBoost: 71.8/100 (92.1% confidence)
- SVM: 64.9/100 (80.0% confidence)
```

#### **Risk Prioritization**
Enhanced STRIDE results automatically prioritize threats:
- **Critical** (8.0+): Immediate emergency response required
- **High** (6.0-7.9): Urgent attention needed
- **Medium** (4.0-5.9): Enhanced monitoring recommended
- **Low** (<4.0): Standard security measures sufficient

---

## 📈 Predictive Risk Evolution

### ML-Driven Temporal Analysis

Temporal analysis uses ML models to predict future risk trends based on historical patterns and current threat intelligence.

#### **Step 1: Navigate to Risk Evolution Tab**
```
📈 Risk Evolution Tab → Temporal Risk Modeling
```

#### **Step 2: Configure Analysis Window**
- **Time Window Options**:
  - `1 Month` - 30 days historical analysis
  - `3 Months` - 90 days pattern recognition
  - `6 Months` - 180 days trend analysis
  - `1 Year` - 365 days comprehensive modeling

#### **Step 3: Generate ML Temporal Analysis**
```
Click: 📊 Generate Risk Timeline
```

**ML-Enhanced Temporal Progress**:
```
📈 ML-Enhanced Temporal Analysis Progress

🔄 Initializing ML-enhanced temporal analysis...
✅ ML models detected - Enhanced temporal prediction enabled

🔄 Generating ML-based historical risk data...
🔄 Running ML predictions across time periods...
🔄 Generating ML-based future predictions...
✅ ML-enhanced temporal analysis completed!

Final ML-Enhanced Results:
- Historical Points: 365
- Future Predictions: 30
- ML Average Risk: 58.7/100
- STRIDE Average Risk: 61.2/100
- ML Volatility: 12.4
- Prediction Accuracy: 92%
```

### Understanding Temporal Predictions

#### **Historical Analysis**
- **ML Risk Scores**: Blue line showing ML-predicted historical risks
- **STRIDE Risk Scores**: Orange line showing enhanced STRIDE historical risks
- **Pattern Recognition**: Seasonal and weekly patterns automatically detected

#### **Future Forecasting**
- **30-Day Predictions**: ML-driven risk forecasting with confidence intervals
- **Trend Analysis**: Automated detection of increasing/decreasing risk trends
- **Early Warning**: Alerts for predicted risk escalations

#### **Key Metrics**
```
Analysis Results:
- ML Trend Slope: +0.023/day (increasing risk)
- STRIDE Trend Slope: +0.018/day (increasing risk)
- ML-STRIDE Correlation: 0.847 (high correlation)
- Prediction Method: ML-Enhanced
```

---

## 🤝 Federated Intelligence

### Privacy-Preserving Multi-Organization Collaboration

Federated learning enables collaborative threat intelligence without sharing sensitive data between organizations.

#### **Step 1: Navigate to Federated Intelligence Tab**
```
🤝 Federated Intelligence Tab → Multi-Organization Intelligence
```

#### **Step 2: Configure Federation**
- **Participants**: 2-4 organizations (simulated)
  - Default organizations: Energy Corp, Manufacturing Ltd, Transport Inc, Utilities Co
- **Privacy Level**: 100% (no data sharing, parameter-only collaboration)
- **Method**: ML-enhanced secure aggregation

#### **Step 3: Simulate Federation**
```
Click: 🔄 Simulate Federation
```

**ML-Enhanced Federation Progress**:
```
🤝 ML-Enhanced Federation Progress

🔄 Initializing ML-enhanced federation network...
✅ ML models detected - Enhanced federated learning enabled

🔄 Loading data for federated training...
🔄 Running federated ML training...
🔄 Training at Energy Corp... (1/4)
🔄 Training at Manufacturing Ltd... (2/4)
🔄 Aggregating ML intelligence across organizations...
✅ ML-enhanced federation completed successfully!

Final ML-Enhanced Results:
- Federation Accuracy: 0.8756
- vs Centralized: 1.008x
- Threat Coverage: 100.0%
- Privacy Level: 100%
- Total Data Samples: 10,000
```

### Federation Benefits

#### **Collective Intelligence**
- **Industry Benchmarking**: Compare your risk levels against industry peers
- **Threat Pattern Sharing**: Learn from collective threat intelligence
- **Privacy Preservation**: No sensitive data leaves your organization
- **Performance Enhancement**: Often matches or exceeds centralized learning

#### **Benchmarking Analytics**
```
🏢 Multi-Organization Benchmarking:
- Industry Average: 72.4/100
- Current Device Risk: 67.3/100
- Percentile Ranking: 67th percentile
- Peer Comparison: Above Average
```

---

## 💡 Adaptive Learning System

### Self-Improving ML Models

The adaptive learning system continuously improves model performance based on security incident feedback.

#### **Step 1: Navigate to Adaptive Models Tab**
```
💡 Adaptive Models Tab → Self-Learning ML Models
```

#### **Step 2: Configure Learning Parameters**
- **Learning Rate**: 0.01-0.5 (controls adaptation speed)
- **Feedback Intensity**: 0.1-2.0 (incident impact strength)
- **Adaptation Method**:
  - `Incremental Learning` - Gradual model improvement
  - `Model Retraining` - Periodic full model updates
  - `Ensemble Weighting` - Dynamic model contribution adjustment

#### **Step 3: Run Adaptive Learning**
```
Click: 🧠 Run ML-Enhanced Adaptive Learning
```

**ML-Enhanced Adaptive Progress**:
```
🧠 ML-Enhanced Adaptive Learning Progress

🔄 Initializing ML-enhanced adaptive learning...
✅ Using trained ML models for adaptive learning

🔄 Generating security incidents for adaptive feedback...
🔄 Running ML adaptive learning with incident feedback...
🔄 Learning iteration 15/24...
✅ ML-enhanced adaptive learning completed!

Final ML-Enhanced Results:
- Total Iterations: 25
- Incidents Processed: 15
- Final Improvement: +0.067 accuracy gain
- Convergence Time: 18 iterations
- Stability Index: 0.94
- Best Model Improvement: +0.089
```

### Learning Mechanisms

#### **Incident-Driven Adaptation**
The system simulates realistic security incidents and learns from prediction accuracy:

```
Security Incident Types:
• DoS Attack (Critical)
• Malware Detection (High)
• Data Exfiltration (High)
• Probe Attack (Medium)
• Normal Activity (Low)
```

#### **Performance Tracking**
- **Convergence Detection**: Automatic identification of optimal learning point
- **Stability Monitoring**: Ensures model improvements don't introduce instability
- **Individual Model Tracking**: Per-model improvement analysis

#### **Learning Results**
```
🤖 ML Model Improvements:
- RandomForest: +0.089
- XGBoost: +0.067
- SVM: +0.045
```

---

## 📊 Advanced Analytics & Reporting

### Unified ML Intelligence Summary

#### **Executive Intelligence Generation**
```
Dashboard → Click: 🚀 Generate ML Intelligence Summary
```

**Sample ML Intelligence Summary**:
```
UNIFIED ML INTELLIGENCE SUMMARY

Risk Assessment: HIGH (7.2/10)
Confidence Level: 100%
ML Components Active: 4/4

KEY FINDINGS:
• ML-Enhanced STRIDE Analysis: ✓
• Federated Threat Intelligence: ✓
• Temporal Risk Projections: ✓
• Adaptive Learning Insights: ✓

INTELLIGENCE INTEGRATION:
This assessment combines machine learning predictions, collaborative threat intelligence,
temporal risk modeling, and adaptive learning feedback to provide comprehensive
cybersecurity risk visibility for industrial IoT environments.

ACTIONABLE INSIGHTS:
• ML Network Analysis detected 67/100 average threat risk
• Industry benchmarking places device in 67th percentile
• Temporal analysis identifies emerging threat patterns for proactive defense
• Adaptive learning identified 3 model improvement opportunities

RECOMMENDATION: Implement integrated ML-driven cybersecurity strategy.
```

### Export & Reporting Capabilities

#### **Available Export Formats**

1. **📥 Download Model Performance**
   ```csv
   Model,Accuracy,CV_Mean,CV_Std,Training_Time
   RandomForest,0.9033,0.8987,0.0123,45.2
   XGBoost,0.8999,0.8945,0.0156,12.8
   SVM,0.8876,0.8821,0.0134,8.7
   ```

2. **📥 Download STRIDE Analysis**
   ```csv
   STRIDE_Category,Likelihood,Impact,Risk_Score,ML_Influence,ML_Enhanced
   Spoofing,6.2,7.0,4.34,0.067,True
   Tampering,7.1,9.0,6.39,0.032,False
   ...
   ```

3. **📊 System Status Report**
   ```
   CIRA-ML SYSTEM STATUS REPORT
   Generated: 2024-12-24 10:30:45

   SYSTEM OVERVIEW
   ---------------
   Data Loaded: True
   Models Trained: 3
   Threat Analysis: True
   Risk Assessments: 5

   MODEL PERFORMANCE
   -----------------
   RandomForest: 0.9033
   XGBoost: 0.8999
   SVM: 0.8876
   ```

---

## 🔧 Troubleshooting & FAQ

### Platform-Specific Solutions

#### **Windows-Specific Issues**

**Q: PowerShell execution policy prevents virtual environment activation**
**A:**
```powershell
# Check current execution policy
Get-ExecutionPolicy

# If Restricted, change to RemoteSigned (recommended)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or use alternative activation
venv\Scripts\activate.bat
```

**Q: "python is not recognized" error on Windows**
**A:**
1. Install Python from microsoft.com/store or python.org
2. Ensure "Add Python to PATH" was checked during installation
3. Restart Command Prompt/PowerShell
4. Use `py` instead of `python` if available

**Q: Dependencies fail to install on Windows**
**A:**
```cmd
# Upgrade pip first
python -m pip install --upgrade pip

# Install with verbose output to identify issues
pip install -r requirements.txt --verbose

# For C++ compilation errors, install Visual Studio Build Tools
# Download from: visualstudio.microsoft.com/visual-cpp-build-tools/
```

**Q: Port access issues on Windows**
**A:**
1. Run Command Prompt as Administrator
2. Check Windows Firewall settings
3. Use alternative port: `streamlit run app.py --server.port 8502`

#### **Linux/macOS-Specific Issues**

**Q: Permission denied when creating virtual environment**
**A:**
```bash
# Use sudo if needed
sudo python3 -m venv cira-ml-env
sudo chown -R $USER:$USER cira-ml-env
```

**Q: Python version conflicts**
**A:**
```bash
# Use specific Python version
python3.9 -m venv cira-ml-env
# or
/usr/bin/python3 -m venv cira-ml-env
```

### Common Issues & Solutions

#### **Q: ML models not training properly**
**A:**
1. Check dataset loading: Ensure data loads successfully in Data Management tab
2. Verify system resources: ML training requires 4GB+ RAM
3. Check error messages in training progress
4. Try training one model at a time to isolate issues

#### **Q: STRIDE analysis shows "No ML models - Using traditional analysis"**
**A:**
1. Ensure models are trained first in Model Training tab
2. Check that training completed successfully (green checkmarks)
3. Verify models are registered in session state
4. Restart browser session if models aren't detected

#### **Q: Federated learning simulation fails**
**A:**
1. Ensure ML models are trained and active
2. Check available system memory (federated learning is memory-intensive)
3. Reduce number of participants if experiencing performance issues
4. Verify network features generation is working

#### **Q: Temporal analysis generates unrealistic predictions**
**A:**
1. This is expected behavior - temporal analysis uses simulated data for demonstration
2. In production, would use actual historical risk data
3. Pattern recognition (seasonal/weekly) is realistic
4. Focus on the ML integration mechanism rather than absolute values

#### **Q: Adaptive learning shows no improvement**
**A:**
1. Increase learning rate for more dramatic changes
2. Adjust feedback intensity for stronger incident impact
3. Run more iterations for convergence
4. Check that incident generation is producing varied scenarios

#### **Q: Save Models button not active after training**
**A:**
1. Ensure all models trained successfully (green checkmarks)
2. Check Model Management section shows "🔥 Freshly trained (can save)"
3. Refresh browser page if button doesn't appear
4. Verify no training errors in progress indicators

#### **Q: Saved models not appearing in dropdown**
**A:**
1. Check if `saved_models/` directory exists in project folder
2. Verify files were saved (look for `cira_models_*.pkl` files)
3. Refresh browser page to reload file list
4. Check file permissions on saved_models directory

#### **Q: Models show as "📂 Loaded from disk" but I want to save them**
**A:**
This is correct behavior - loaded models are already saved and don't need re-saving:
1. Models loaded from disk cannot be saved again (prevents duplicates)
2. To save new models: Train fresh models → Save button becomes active
3. This prevents accidental duplicate model files

#### **Q: Auto-loaded models don't work**
**A:**
1. Check if models auto-loaded (toast notification appears)
2. Verify Current Session shows "📂 Loaded from disk"
3. If auto-load failed, manually load via dropdown
4. Check saved model files aren't corrupted

### Performance Optimization

#### **Memory Usage Guidelines**
- **Minimum**: 8GB RAM for basic functionality
- **Recommended**: 16GB+ RAM for full ML capabilities
- **Large Datasets**: 32GB+ RAM for datasets >500K samples

#### **Training Time Expectations**
- **Small Dataset** (<50K samples): 30-60 seconds per model
- **Medium Dataset** (50K-200K): 1-3 minutes per model
- **Large Dataset** (200K+): 3-10 minutes per model

#### **Browser Compatibility**
- **Recommended**: Chrome, Firefox, Safari (latest versions)
- **Avoid**: Internet Explorer, older browser versions
- **JavaScript**: Must be enabled for interactive features

### Advanced Configuration

#### **Environment Variables**
```bash
# Performance tuning
export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
export STREAMLIT_SERVER_MAX_MESSAGE_SIZE=200

# Security settings
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true
```

#### **Memory Optimization**
```python
# For large datasets, consider:
- Reducing cross-validation folds (3 instead of 5)
- Using subset training for SVM (automatic)
- Training models sequentially instead of parallel
- Clearing browser cache regularly
```

---

## 🎯 Best Practices

### ML-Enhanced Workflow Recommendations

1. **Start Simple**: Begin with one dataset and all three models
2. **Verify Training**: Always check training results before proceeding to analysis
3. **Compare Results**: Use traditional vs ML-enhanced analysis comparison
4. **Export Data**: Save results for further analysis and reporting
5. **Monitor Performance**: Track system health and component status

### Industrial IoT Security Assessment Workflow

```
1. Data Collection → Load network traffic data (UNSW-NB15/IoT-23)
2. ML Training → Train ensemble models (RF + XGBoost + SVM)
3. Device Analysis → Run ML-enhanced STRIDE for specific device types
4. Temporal Assessment → Analyze risk evolution and future predictions
5. Industry Benchmarking → Compare with federated intelligence
6. Continuous Learning → Enable adaptive feedback for model improvement
7. Executive Reporting → Generate ML intelligence summaries
```

### Security Considerations

- **Data Privacy**: All processing is local, no data transmitted externally
- **Model Security**: Trained models remain in browser session only
- **Access Control**: Implement appropriate network access controls
- **Audit Trail**: Export and archive analysis results for compliance
- **Regular Updates**: Keep dependencies and datasets current

---

**Usage Guide Version**: 2.0
**Last Updated**: December 2024
**For Technical Support**: Refer to technical documentation and implementation report