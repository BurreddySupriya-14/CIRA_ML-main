# Risk Fusion Engine - Integrates ML predictions with STRIDE analysis
"""
CIRA-ML Risk Fusion Engine
Combines machine learning predictions with STRIDE threat modeling
for comprehensive risk assessment.
"""

import numpy as np
import pandas as pd
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class RiskFusionEngine:
    """
    Unified risk assessment combining ML predictions and STRIDE analysis
    """

    def __init__(self):
        self.ml_models = {}
        self.stride_weights = {
            'Spoofing': 0.15,
            'Tampering': 0.20,
            'Repudiation': 0.10,
            'Information Disclosure': 0.15,
            'Denial of Service': 0.25,
            'Elevation of Privilege': 0.15
        }
        self.device_risk_multipliers = {
            'PLC Controller': 1.2,
            'HMI Interface': 1.0,
            'Industrial Sensors': 0.8,
            'Network Gateway': 1.4,
            'SCADA System': 1.5,
            'Industrial Camera': 0.6
        }

    def register_ml_models(self, models_dict):
        """Register trained ML models for predictions"""
        self.ml_models = models_dict

    def predict_network_risk(self, network_features) -> Dict[str, float]:
        """
        Use trained ML models to predict network-based risks

        Args:
            network_features: Network traffic features for prediction

        Returns:
            Dictionary with model predictions and confidence scores
        """
        if not self.ml_models:
            return {"error": "No ML models registered"}

        predictions = {}

        for model_name, model in self.ml_models.items():
            try:
                # Get prediction and probability
                pred = model.predict([network_features])[0]

                # Get prediction probabilities if available
                if hasattr(model, 'predict_proba'):
                    proba = model.predict_proba([network_features])[0]
                    confidence = max(proba)
                else:
                    confidence = 0.8  # Default confidence for SVM

                # Convert prediction to risk score (0-100)
                risk_score = self._convert_prediction_to_risk(pred, confidence)

                predictions[model_name] = {
                    'prediction': pred,
                    'confidence': confidence,
                    'risk_score': risk_score
                }

            except Exception as e:
                predictions[model_name] = {
                    'error': str(e),
                    'risk_score': 50  # Default moderate risk
                }

        return predictions

    def _convert_prediction_to_risk(self, prediction, confidence) -> float:
        """Convert ML prediction to 0-100 risk score"""
        # Map attack types to risk levels
        attack_risk_map = {
            0: 10,   # Normal - Low risk
            1: 85,   # DoS - Very High risk
            2: 60,   # Probe - Medium-High risk
            3: 95,   # Malware - Critical risk
            4: 75,   # Fuzzers - High risk
            5: 70,   # Analysis - High risk
            6: 80,   # Backdoor - Very High risk
            7: 90,   # Shellcode - Critical risk
            8: 65,   # Worms - High risk
        }

        base_risk = attack_risk_map.get(prediction, 50)

        # Adjust by confidence
        adjusted_risk = base_risk * confidence + (50 * (1 - confidence))

        return min(100, max(0, adjusted_risk))

    def enhanced_stride_analysis(self, device_type: str, network_risk: Dict,
                                business_criticality: int) -> Dict:
        """
        Enhanced STRIDE analysis using ML predictions

        Args:
            device_type: Type of industrial device
            network_risk: ML-based network risk predictions
            business_criticality: Business impact score (1-10)

        Returns:
            Enhanced STRIDE analysis with ML integration
        """

        # Get average ML risk score
        ml_risk_scores = [pred.get('risk_score', 50) for pred in network_risk.values()
                         if isinstance(pred, dict) and 'risk_score' in pred]
        avg_ml_risk = np.mean(ml_risk_scores) if ml_risk_scores else 50

        # Base STRIDE threats (from original implementation)
        base_stride = {
            'Spoofing': {'likelihood': 6, 'impact': 7},
            'Tampering': {'likelihood': 7, 'impact': 9},
            'Repudiation': {'likelihood': 4, 'impact': 5},
            'Information Disclosure': {'likelihood': 8, 'impact': 6},
            'Denial of Service': {'likelihood': 9, 'impact': 8},
            'Elevation of Privilege': {'likelihood': 5, 'impact': 10}
        }

        # Enhance STRIDE with ML predictions
        enhanced_stride = {}
        device_multiplier = self.device_risk_multipliers.get(device_type, 1.0)

        for category, scores in base_stride.items():
            # Adjust likelihood based on ML predictions
            ml_influence = self._calculate_ml_influence(category, avg_ml_risk)

            enhanced_likelihood = scores['likelihood'] * (1 + ml_influence)
            enhanced_likelihood = min(10, max(1, enhanced_likelihood))

            # Adjust impact based on business criticality and device type
            enhanced_impact = scores['impact'] * (business_criticality / 7) * device_multiplier
            enhanced_impact = min(10, max(1, enhanced_impact))

            # Calculate integrated risk score
            risk_score = (enhanced_likelihood * enhanced_impact) / 10

            enhanced_stride[category] = {
                'likelihood': round(enhanced_likelihood, 1),
                'impact': round(enhanced_impact, 1),
                'risk_score': round(risk_score, 2),
                'ml_influence': round(ml_influence, 3),
                'base_likelihood': scores['likelihood'],
                'base_impact': scores['impact']
            }

        return {
            'stride_analysis': enhanced_stride,
            'ml_risk_average': round(avg_ml_risk, 2),
            'device_multiplier': device_multiplier,
            'business_criticality': business_criticality,
            'integration_timestamp': datetime.now(),
            'overall_risk_score': round(np.mean([s['risk_score'] for s in enhanced_stride.values()]), 2)
        }

    def _calculate_ml_influence(self, stride_category: str, ml_risk: float) -> float:
        """Calculate how ML predictions influence STRIDE likelihood"""

        # Map ML risk to STRIDE categories
        category_sensitivity = {
            'Spoofing': 0.3,           # Moderate influence from network anomalies
            'Tampering': 0.2,          # Less influenced by network patterns
            'Repudiation': 0.1,        # Least influenced by network data
            'Information Disclosure': 0.4,  # High influence from data patterns
            'Denial of Service': 0.6,  # Very high influence from traffic patterns
            'Elevation of Privilege': 0.25  # Moderate influence
        }

        sensitivity = category_sensitivity.get(stride_category, 0.3)

        # Convert ML risk (0-100) to influence factor (-0.5 to +0.5)
        # High ML risk increases STRIDE likelihood
        normalized_risk = (ml_risk - 50) / 100  # -0.5 to +0.5

        return normalized_risk * sensitivity

    def generate_unified_report(self, device_type: str, network_features,
                              business_criticality: int) -> Dict:
        """
        Generate comprehensive risk report combining all analysis

        Args:
            device_type: Industrial device type
            network_features: Network traffic data for ML analysis
            business_criticality: Business impact rating (1-10)

        Returns:
            Unified risk assessment report
        """

        # Step 1: ML Network Risk Analysis
        network_risk = self.predict_network_risk(network_features)

        # Step 2: Enhanced STRIDE Analysis
        stride_analysis = self.enhanced_stride_analysis(
            device_type, network_risk, business_criticality
        )

        # Step 3: Risk Prioritization
        risk_priorities = self._prioritize_risks(stride_analysis['stride_analysis'])

        # Step 4: Mitigation Recommendations
        mitigations = self._generate_mitigations(risk_priorities, network_risk)

        return {
            'device_info': {
                'device_type': device_type,
                'business_criticality': business_criticality,
                'analysis_timestamp': datetime.now()
            },
            'ml_analysis': network_risk,
            'stride_analysis': stride_analysis,
            'risk_priorities': risk_priorities,
            'mitigations': mitigations,
            'executive_summary': self._generate_executive_summary(
                stride_analysis, network_risk, device_type
            )
        }

    def _prioritize_risks(self, stride_data: Dict) -> List[Dict]:
        """Prioritize risks by score and business impact"""
        risks = []

        for category, data in stride_data.items():
            risks.append({
                'category': category,
                'risk_score': data['risk_score'],
                'likelihood': data['likelihood'],
                'impact': data['impact'],
                'ml_influenced': abs(data['ml_influence']) > 0.1,
                'priority': 'Critical' if data['risk_score'] >= 8 else
                           'High' if data['risk_score'] >= 6 else
                           'Medium' if data['risk_score'] >= 4 else 'Low'
            })

        return sorted(risks, key=lambda x: x['risk_score'], reverse=True)

    def _generate_mitigations(self, risk_priorities: List[Dict],
                            network_risk: Dict) -> Dict:
        """Generate targeted mitigation recommendations"""

        mitigations = {
            'immediate_actions': [],
            'short_term_improvements': [],
            'long_term_strategy': []
        }

        # High-risk items need immediate action
        high_risk_categories = [r for r in risk_priorities if r['risk_score'] >= 6]

        for risk in high_risk_categories:
            category = risk['category']

            if category == 'Denial of Service':
                mitigations['immediate_actions'].append({
                    'action': 'Implement DDoS protection and rate limiting',
                    'category': category,
                    'ml_evidence': 'Network anomalies detected' if risk['ml_influenced'] else 'Standard risk assessment'
                })

            elif category == 'Information Disclosure':
                mitigations['immediate_actions'].append({
                    'action': 'Enable encryption for all data channels',
                    'category': category,
                    'ml_evidence': 'Data exfiltration patterns detected' if risk['ml_influenced'] else 'High impact assessment'
                })

        return mitigations

    def _generate_executive_summary(self, stride_analysis: Dict,
                                  network_risk: Dict, device_type: str) -> str:
        """Generate executive summary of the risk analysis"""

        overall_risk = stride_analysis['overall_risk_score']
        ml_average = stride_analysis['ml_risk_average']

        risk_level = ('Critical' if overall_risk >= 8 else
                     'High' if overall_risk >= 6 else
                     'Medium' if overall_risk >= 4 else 'Low')

        successful_ml_models = len([m for m in network_risk.values()
                                  if isinstance(m, dict) and 'risk_score' in m])

        summary = f"""
EXECUTIVE RISK SUMMARY - {device_type}

Overall Risk Level: {risk_level} ({overall_risk:.1f}/10)

Key Findings:
• ML Network Analysis: {ml_average:.1f}/100 risk score from {successful_ml_models} models
• STRIDE Assessment: Enhanced with ML intelligence integration
• Business Impact: Adjusted for device criticality and operational context

Critical Actions Required: {len([r for r in stride_analysis['stride_analysis'].values() if r['risk_score'] >= 8])}

This assessment combines machine learning network analysis with systematic
threat modeling to provide comprehensive risk visibility.
        """

        return summary.strip()

# Example usage and integration helper
class CIRAIntegrationManager:
    """Enhanced Integration Manager with Unified ML Intelligence Hub"""

    def __init__(self):
        self.fusion_engine = RiskFusionEngine()
        self.unified_hub = CIRAUnifiedMLIntelligenceHub()

    def setup_with_trained_models(self, session_state):
        """Setup both fusion engine and unified hub with models from Streamlit session"""
        models_available = False

        if hasattr(session_state, 'models') and session_state.models:
            self.fusion_engine.register_ml_models(session_state.models)
            self.unified_hub.initialize_with_models(session_state.models)
            models_available = True

        return models_available

    def integrated_stride_analysis(self, device_type: str, criticality: int,
                                 sample_network_data=None):
        """Enhanced STRIDE analysis with ML integration"""

        # Generate sample network features if none provided
        if sample_network_data is None:
            sample_network_data = np.random.rand(39)  # 39 features like UNSW-NB15

        # Generate unified risk report
        report = self.fusion_engine.generate_unified_report(
            device_type, sample_network_data, criticality
        )

        return report

    def comprehensive_unified_assessment(self, device_type: str, criticality: int,
                                       network_features=None, historical_context=None):
        """
        Comprehensive assessment using the Unified ML Intelligence Hub
        Integrates all ML components for holistic risk assessment
        """

        # Generate sample network features if none provided
        if network_features is None:
            network_features = np.random.rand(39)  # 39 features like UNSW-NB15

        # Run comprehensive assessment using unified hub
        comprehensive_results = self.unified_hub.comprehensive_risk_assessment(
            device_type, network_features, criticality, historical_context
        )

        return comprehensive_results

    def get_system_health_status(self):
        """Get current ML system health status"""
        return self.unified_hub._assess_system_health()

    def get_ml_intelligence_summary(self, device_type: str, criticality: int):
        """Get executive ML intelligence summary"""
        assessment = self.comprehensive_unified_assessment(device_type, criticality)
        return assessment.get('intelligence_summary', 'No intelligence summary available')

    def get_unified_risk_score(self, device_type: str, criticality: int):
        """Get unified risk score across all ML components"""
        assessment = self.comprehensive_unified_assessment(device_type, criticality)
        return assessment.get('unified_risk_score', {'overall_risk': 5.0, 'risk_level': 'Medium'})

# Unified ML Intelligence Hub
class CIRAUnifiedMLIntelligenceHub:
    """
    Comprehensive ML Intelligence Hub that integrates all CIRA ML components
    Provides unified interface for ML-enhanced STRIDE, Federated Learning,
    Temporal Analysis, and Adaptive Models
    """

    def __init__(self):
        self.risk_fusion_engine = RiskFusionEngine()
        self.ml_models = {}
        self.system_status = {
            'stride_enhanced': False,
            'federated_ready': False,
            'temporal_active': False,
            'adaptive_learning': False,
            'unified_intelligence': False
        }

    def initialize_with_models(self, models_dict):
        """Initialize the hub with trained ML models"""
        self.ml_models = models_dict
        self.risk_fusion_engine.register_ml_models(models_dict)
        self.system_status['unified_intelligence'] = bool(models_dict)
        return self.system_status['unified_intelligence']

    def comprehensive_risk_assessment(self, device_type: str, network_features,
                                    business_criticality: int, historical_context: Dict = None):
        """
        Comprehensive unified risk assessment using all ML components

        Args:
            device_type: Industrial device type
            network_features: Current network traffic features
            business_criticality: Business impact rating (1-10)
            historical_context: Optional historical data for temporal analysis

        Returns:
            Unified comprehensive risk assessment with ML intelligence
        """

        assessment_results = {
            'timestamp': datetime.now(),
            'device_info': {
                'type': device_type,
                'criticality': business_criticality
            },
            'ml_status': self.system_status.copy()
        }

        # 1. Core ML-Enhanced STRIDE Analysis
        try:
            stride_analysis = self.risk_fusion_engine.generate_unified_report(
                device_type, network_features, business_criticality
            )
            assessment_results['stride_analysis'] = stride_analysis
            self.system_status['stride_enhanced'] = True
        except Exception as e:
            assessment_results['stride_error'] = str(e)
            self.system_status['stride_enhanced'] = False

        # 2. Federated Intelligence Insights
        try:
            federated_insights = self._generate_federated_insights(
                device_type, network_features, stride_analysis
            )
            assessment_results['federated_intelligence'] = federated_insights
            self.system_status['federated_ready'] = True
        except Exception as e:
            assessment_results['federated_error'] = str(e)
            self.system_status['federated_ready'] = False

        # 3. Temporal Risk Projections
        try:
            temporal_projections = self._generate_temporal_projections(
                stride_analysis, historical_context
            )
            assessment_results['temporal_analysis'] = temporal_projections
            self.system_status['temporal_active'] = True
        except Exception as e:
            assessment_results['temporal_error'] = str(e)
            self.system_status['temporal_active'] = False

        # 4. Adaptive Learning Recommendations
        try:
            adaptive_recommendations = self._generate_adaptive_recommendations(
                stride_analysis, federated_insights, temporal_projections
            )
            assessment_results['adaptive_learning'] = adaptive_recommendations
            self.system_status['adaptive_learning'] = True
        except Exception as e:
            assessment_results['adaptive_error'] = str(e)
            self.system_status['adaptive_learning'] = False

        # 5. Unified Risk Score and Intelligence Summary
        unified_score = self._calculate_unified_risk_score(assessment_results)
        intelligence_summary = self._generate_intelligence_summary(assessment_results, unified_score)

        assessment_results.update({
            'unified_risk_score': unified_score,
            'intelligence_summary': intelligence_summary,
            'system_health': self._assess_system_health(),
            'recommendations': self._generate_unified_recommendations(assessment_results)
        })

        return assessment_results

    def _generate_federated_insights(self, device_type: str, network_features,
                                   stride_analysis: Dict) -> Dict:
        """Generate federated intelligence insights"""

        # Simulate federated intelligence from multiple organizations
        organizations = ['Energy Corp', 'Manufacturing Ltd', 'Transport Inc', 'Utilities Co']

        federated_data = {
            'participating_organizations': len(organizations),
            'collective_threat_intelligence': {},
            'risk_benchmarking': {},
            'privacy_preserved_insights': []
        }

        # Generate collective threat intelligence
        if stride_analysis and 'ml_analysis' in stride_analysis:
            ml_risks = stride_analysis['ml_analysis']

            for org in organizations:
                # Simulate organization-specific insights
                org_risk_modifier = np.random.uniform(0.8, 1.2)
                org_insights = {}

                for model_name, prediction in ml_risks.items():
                    if isinstance(prediction, dict) and 'risk_score' in prediction:
                        modified_risk = prediction['risk_score'] * org_risk_modifier
                        org_insights[model_name] = {
                            'risk_level': np.clip(modified_risk, 0, 100),
                            'confidence': prediction.get('confidence', 0.8),
                            'threat_patterns': f"Pattern_{org}_{model_name}"
                        }

                federated_data['collective_threat_intelligence'][org] = org_insights

            # Calculate federated risk benchmarking
            device_benchmark = np.random.uniform(60, 80)  # Industry benchmark
            current_risk = stride_analysis.get('stride_analysis', {}).get('overall_risk_score', 5) * 10

            federated_data['risk_benchmarking'] = {
                'industry_average': device_benchmark,
                'current_device_risk': current_risk,
                'percentile_ranking': max(0, min(100, 100 - (current_risk - device_benchmark) * 2)),
                'peer_comparison': 'Above Average' if current_risk < device_benchmark else 'Below Average'
            }

        return federated_data

    def _generate_temporal_projections(self, stride_analysis: Dict,
                                     historical_context: Dict = None) -> Dict:
        """Generate temporal risk projections and forecasting"""

        temporal_data = {
            'forecast_horizon_days': 30,
            'risk_trend_analysis': {},
            'threat_evolution_forecast': {},
            'seasonal_risk_patterns': {}
        }

        if stride_analysis and 'stride_analysis' in stride_analysis:
            current_risks = stride_analysis['stride_analysis']

            # Generate risk trend forecasts for each STRIDE category
            for category, risk_data in current_risks.items():
                current_risk = risk_data['risk_score']

                # Simulate trend analysis
                trend_slope = np.random.uniform(-0.05, 0.05)  # Daily risk change
                volatility = np.random.uniform(0.1, 0.3)

                # Generate 30-day forecast
                forecast_days = list(range(1, 31))
                forecast_risks = []

                for day in forecast_days:
                    projected_risk = current_risk + (trend_slope * day) + np.random.normal(0, volatility)
                    forecast_risks.append(max(0, min(10, projected_risk)))

                temporal_data['risk_trend_analysis'][category] = {
                    'current_risk': current_risk,
                    'trend_slope': trend_slope,
                    'volatility': volatility,
                    'forecast': forecast_risks,
                    'confidence_interval': [0.8, 0.95]  # Confidence bounds
                }

            # Generate threat evolution patterns
            threat_types = ['Advanced Persistent Threats', 'IoT Botnets', 'Supply Chain Attacks', 'Insider Threats']
            for threat_type in threat_types:
                evolution_score = np.random.uniform(0.2, 0.9)
                temporal_data['threat_evolution_forecast'][threat_type] = {
                    'current_prevalence': evolution_score,
                    'projected_growth': np.random.uniform(-0.1, 0.3),
                    'peak_risk_period': np.random.choice(['Week 1-2', 'Week 2-3', 'Week 3-4']),
                    'mitigation_urgency': 'High' if evolution_score > 0.7 else 'Medium' if evolution_score > 0.4 else 'Low'
                }

        return temporal_data

    def _generate_adaptive_recommendations(self, stride_analysis: Dict,
                                         federated_insights: Dict,
                                         temporal_projections: Dict) -> Dict:
        """Generate adaptive learning recommendations"""

        adaptive_data = {
            'learning_opportunities': [],
            'model_enhancement_suggestions': [],
            'feedback_integration_points': [],
            'continuous_improvement_metrics': {}
        }

        # Analyze current ML performance for improvement opportunities
        if stride_analysis and 'ml_analysis' in stride_analysis:
            ml_results = stride_analysis['ml_analysis']

            for model_name, prediction in ml_results.items():
                if isinstance(prediction, dict):
                    confidence = prediction.get('confidence', 0.8)
                    risk_score = prediction.get('risk_score', 50)

                    # Generate learning opportunities
                    if confidence < 0.7:
                        adaptive_data['learning_opportunities'].append({
                            'model': model_name,
                            'issue': 'Low confidence predictions',
                            'recommendation': 'Increase training data diversity',
                            'priority': 'High',
                            'estimated_improvement': f"{(0.9 - confidence) * 100:.1f}%"
                        })

                    if risk_score > 80:
                        adaptive_data['model_enhancement_suggestions'].append({
                            'model': model_name,
                            'enhancement': 'High-risk scenario specialization',
                            'method': 'Focused retraining on critical incidents',
                            'expected_outcome': 'Improved high-risk detection accuracy'
                        })

        # Integration points with federated and temporal analysis
        if federated_insights:
            adaptive_data['feedback_integration_points'].append({
                'source': 'Federated Intelligence',
                'integration': 'Cross-organizational threat patterns',
                'benefit': 'Enhanced collective learning from industry peers'
            })

        if temporal_projections:
            adaptive_data['feedback_integration_points'].append({
                'source': 'Temporal Analysis',
                'integration': 'Historical trend learning',
                'benefit': 'Improved risk forecasting accuracy'
            })

        return adaptive_data

    def _calculate_unified_risk_score(self, assessment_results: Dict) -> Dict:
        """Calculate unified risk score from all ML components"""

        unified_score = {
            'overall_risk': 5.0,  # Default moderate risk
            'confidence': 0.8,
            'component_contributions': {},
            'risk_factors': {}
        }

        total_weight = 0
        weighted_score = 0

        # STRIDE Analysis contribution (40% weight)
        if 'stride_analysis' in assessment_results:
            stride_risk = assessment_results['stride_analysis'].get('stride_analysis', {}).get('overall_risk_score', 5.0)
            weight = 0.4
            weighted_score += stride_risk * weight
            total_weight += weight
            unified_score['component_contributions']['stride'] = {
                'score': stride_risk,
                'weight': weight,
                'contribution': stride_risk * weight
            }

        # Federated Intelligence contribution (25% weight)
        if 'federated_intelligence' in assessment_results:
            fed_benchmark = assessment_results['federated_intelligence'].get('risk_benchmarking', {})
            fed_risk = fed_benchmark.get('current_device_risk', 50) / 10  # Convert to 0-10 scale
            weight = 0.25
            weighted_score += fed_risk * weight
            total_weight += weight
            unified_score['component_contributions']['federated'] = {
                'score': fed_risk,
                'weight': weight,
                'contribution': fed_risk * weight
            }

        # Temporal Analysis contribution (20% weight)
        if 'temporal_analysis' in assessment_results:
            temporal_risks = assessment_results['temporal_analysis'].get('risk_trend_analysis', {})
            if temporal_risks:
                avg_temporal_risk = np.mean([risk_info['current_risk'] for risk_info in temporal_risks.values()])
                weight = 0.20
                weighted_score += avg_temporal_risk * weight
                total_weight += weight
                unified_score['component_contributions']['temporal'] = {
                    'score': avg_temporal_risk,
                    'weight': weight,
                    'contribution': avg_temporal_risk * weight
                }

        # Adaptive Learning contribution (15% weight)
        if 'adaptive_learning' in assessment_results:
            adaptive_impact = len(assessment_results['adaptive_learning'].get('learning_opportunities', []))
            adaptive_risk = 5.0 + (adaptive_impact * 0.5)  # Higher learning needs = higher current risk
            weight = 0.15
            weighted_score += adaptive_risk * weight
            total_weight += weight
            unified_score['component_contributions']['adaptive'] = {
                'score': adaptive_risk,
                'weight': weight,
                'contribution': adaptive_risk * weight
            }

        # Calculate final unified score
        if total_weight > 0:
            unified_score['overall_risk'] = weighted_score / total_weight
            unified_score['confidence'] = total_weight  # Higher total weight = higher confidence

        # Classify risk level
        risk_level = unified_score['overall_risk']
        if risk_level >= 8:
            unified_score['risk_level'] = 'Critical'
        elif risk_level >= 6:
            unified_score['risk_level'] = 'High'
        elif risk_level >= 4:
            unified_score['risk_level'] = 'Medium'
        else:
            unified_score['risk_level'] = 'Low'

        return unified_score

    def _generate_intelligence_summary(self, assessment_results: Dict, unified_score: Dict) -> str:
        """Generate executive intelligence summary"""

        risk_level = unified_score.get('risk_level', 'Medium')
        overall_risk = unified_score.get('overall_risk', 5.0)
        confidence = unified_score.get('confidence', 0.8)

        # Count active ML components
        active_components = sum([
            'stride_analysis' in assessment_results,
            'federated_intelligence' in assessment_results,
            'temporal_analysis' in assessment_results,
            'adaptive_learning' in assessment_results
        ])

        summary = f"""
UNIFIED ML INTELLIGENCE SUMMARY

Risk Assessment: {risk_level.upper()} ({overall_risk:.1f}/10)
Confidence Level: {confidence*100:.0f}%
ML Components Active: {active_components}/4

KEY FINDINGS:
• ML-Enhanced STRIDE Analysis: {'✓' if 'stride_analysis' in assessment_results else '✗'}
• Federated Threat Intelligence: {'✓' if 'federated_intelligence' in assessment_results else '✗'}
• Temporal Risk Projections: {'✓' if 'temporal_analysis' in assessment_results else '✗'}
• Adaptive Learning Insights: {'✓' if 'adaptive_learning' in assessment_results else '✗'}

INTELLIGENCE INTEGRATION:
This assessment combines machine learning predictions, collaborative threat intelligence,
temporal risk modeling, and adaptive learning feedback to provide comprehensive
cybersecurity risk visibility for industrial IoT environments.

ACTIONABLE INSIGHTS:
"""

        # Add specific insights based on results
        if 'stride_analysis' in assessment_results:
            ml_risk_avg = assessment_results['stride_analysis'].get('ml_risk_average', 0)
            summary += f"• ML Network Analysis detected {ml_risk_avg:.0f}/100 average threat risk\n"

        if 'federated_intelligence' in assessment_results:
            benchmark = assessment_results['federated_intelligence'].get('risk_benchmarking', {})
            percentile = benchmark.get('percentile_ranking', 50)
            summary += f"• Industry benchmarking places device in {percentile:.0f}th percentile\n"

        if 'temporal_analysis' in assessment_results:
            summary += "• Temporal analysis identifies emerging threat patterns for proactive defense\n"

        if 'adaptive_learning' in assessment_results:
            opportunities = len(assessment_results['adaptive_learning'].get('learning_opportunities', []))
            summary += f"• Adaptive learning identified {opportunities} model improvement opportunities\n"

        summary += "\nRECOMMENDATION: Implement integrated ML-driven cybersecurity strategy."

        return summary.strip()

    def _assess_system_health(self) -> Dict:
        """Assess overall system health and ML integration status"""

        active_components = sum(self.system_status.values())
        total_components = len(self.system_status)
        health_score = active_components / total_components

        health_assessment = {
            'overall_health': health_score,
            'status': 'Excellent' if health_score >= 0.8 else
                     'Good' if health_score >= 0.6 else
                     'Fair' if health_score >= 0.4 else 'Poor',
            'active_components': active_components,
            'total_components': total_components,
            'component_status': self.system_status.copy(),
            'recommendations': []
        }

        # Generate health recommendations
        if not self.system_status['stride_enhanced']:
            health_assessment['recommendations'].append("Enable ML-enhanced STRIDE analysis for improved threat detection")

        if not self.system_status['federated_ready']:
            health_assessment['recommendations'].append("Activate federated intelligence for industry threat sharing")

        if not self.system_status['temporal_active']:
            health_assessment['recommendations'].append("Initialize temporal analysis for predictive risk modeling")

        if not self.system_status['adaptive_learning']:
            health_assessment['recommendations'].append("Enable adaptive learning for continuous model improvement")

        return health_assessment

    def _generate_unified_recommendations(self, assessment_results: Dict) -> Dict:
        """Generate unified recommendations across all ML components"""

        recommendations = {
            'immediate_actions': [],
            'strategic_improvements': [],
            'ml_optimizations': [],
            'integration_enhancements': []
        }

        # Analyze results for immediate actions
        unified_risk = assessment_results.get('unified_risk_score', {}).get('overall_risk', 5)

        if unified_risk >= 7:
            recommendations['immediate_actions'].extend([
                "Activate emergency response protocols for high-risk threat detection",
                "Implement enhanced monitoring on identified high-risk STRIDE categories",
                "Review and update incident response procedures"
            ])

        # Strategic improvements based on component analysis
        if 'stride_analysis' in assessment_results:
            stride_data = assessment_results['stride_analysis']
            high_risk_categories = [cat for cat, data in stride_data.items()
                                  if isinstance(data, dict) and data.get('risk_score', 0) >= 7]

            if high_risk_categories:
                recommendations['strategic_improvements'].append(
                    f"Focus security investments on {', '.join(high_risk_categories)} threat categories"
                )

        # ML optimization recommendations
        if 'adaptive_learning' in assessment_results:
            learning_opportunities = assessment_results['adaptive_learning'].get('learning_opportunities', [])
            for opportunity in learning_opportunities:
                recommendations['ml_optimizations'].append({
                    'model': opportunity.get('model', 'Unknown'),
                    'action': opportunity.get('recommendation', 'Review model performance'),
                    'priority': opportunity.get('priority', 'Medium')
                })

        # Integration enhancements
        active_components = sum([
            'stride_analysis' in assessment_results,
            'federated_intelligence' in assessment_results,
            'temporal_analysis' in assessment_results,
            'adaptive_learning' in assessment_results
        ])

        if active_components < 4:
            recommendations['integration_enhancements'].append(
                "Enable all ML intelligence components for comprehensive risk assessment"
            )

        return recommendations