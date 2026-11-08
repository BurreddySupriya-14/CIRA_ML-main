# src/threat_modeling/risk_calculator.py
import numpy as np


class RiskCalculator:
    """Calculate risk scores for IIoT devices"""

    def __init__(self, high_threshold=7.0, medium_threshold=4.0):
        self.high_threshold = high_threshold
        self.medium_threshold = medium_threshold

    def calculate_risk_score(self, cvss_score, exploitability, asset_value):
        """
        Calculate risk score: Risk = Asset × Vulnerability × Threat
        """
        vulnerability = cvss_score / 10.0
        threat = exploitability / 10.0
        risk_score = asset_value * vulnerability * threat * 10
        return min(risk_score, 100)  # Cap at 100

    def categorize_risk(self, risk_score):
        """Categorize risk based on score"""
        if risk_score >= 80:
            return "Very High", 1.0
        elif risk_score >= 60:
            return "High", 0.8
        elif risk_score >= 40:
            return "Medium", 0.5
        elif risk_score >= 20:
            return "Low", 0.2
        else:
            return "Very Low", 0.1

    def assess_device(self, device_name, cvss, exploit, asset):
        """Complete assessment for a device"""
        risk_score = self.calculate_risk_score(cvss, exploit, asset)
        risk_level, risk_weight = self.categorize_risk(risk_score)

        return {
            'device': device_name,
            'cvss': cvss,
            'exploitability': exploit,
            'asset_value': asset,
            'risk_score': round(risk_score, 2),
            'risk_level': risk_level,
            'risk_weight': risk_weight
        }


# Test functionality
if __name__ == "__main__":
    calc = RiskCalculator()

    test_cases = [
        ("PLC Controller", 7.5, 8.0, 9.0),
        ("IoT Sensor", 4.2, 5.0, 3.0),
    ]

    for name, cvss, exp, asset in test_cases:
        score = calc.calculate_risk_score(cvss, exp, asset)
        level, weight = calc.categorize_risk(score)
        # Test validation only - no output in production