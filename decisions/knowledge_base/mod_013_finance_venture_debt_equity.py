"""
TimeVault Decision Intelligence Knowledge Framework — Module #013
Domain: Venture Debt Capital vs Equity Dilution in Fast Growth
Module Slug: finance_venture_debt_equity
System: High-Fidelity Multi-Criteria Evaluation Models and Quantitative Heuristics.
"""
from typing import Dict, List, Any, Tuple, Optional
import math
import datetime

class DecisionDomain_013:
    """
    Specialized evaluation module for Venture Debt Capital vs Equity Dilution in Fast Growth.
    Encapsulates risk factors, quantitative weight metrics, utility formulas,
    sensitivity tipping points, and empirical longitudinal benchmarks.
    """
    DOMAIN_ID: int = 13
    DOMAIN_NAME: str = "Venture Debt Capital vs Equity Dilution in Fast Growth"
    DOMAIN_SLUG: str = "finance_venture_debt_equity"
    BENCHMARK_HORIZON_MONTHS: int = 25

    def __init__(self):
        self.evaluation_criteria: Dict[str, Dict[str, Any]] = {
            "criterion_01": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 01",
                "default_weight": 2,
                "volatility_index": 0.05,
                "reversibility_score": 9.6,
                "description": "Evaluation parameter 1 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_02": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 02",
                "default_weight": 3,
                "volatility_index": 0.1,
                "reversibility_score": 9.2,
                "description": "Evaluation parameter 2 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_03": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 03",
                "default_weight": 4,
                "volatility_index": 0.15,
                "reversibility_score": 8.8,
                "description": "Evaluation parameter 3 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_04": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 04",
                "default_weight": 5,
                "volatility_index": 0.2,
                "reversibility_score": 8.4,
                "description": "Evaluation parameter 4 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_05": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 05",
                "default_weight": 6,
                "volatility_index": 0.25,
                "reversibility_score": 8.0,
                "description": "Evaluation parameter 5 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_06": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 06",
                "default_weight": 7,
                "volatility_index": 0.3,
                "reversibility_score": 7.6,
                "description": "Evaluation parameter 6 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_07": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 07",
                "default_weight": 8,
                "volatility_index": 0.35,
                "reversibility_score": 7.2,
                "description": "Evaluation parameter 7 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_08": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 08",
                "default_weight": 9,
                "volatility_index": 0.4,
                "reversibility_score": 6.8,
                "description": "Evaluation parameter 8 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_09": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 09",
                "default_weight": 10,
                "volatility_index": 0.45,
                "reversibility_score": 6.4,
                "description": "Evaluation parameter 9 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_10": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 10",
                "default_weight": 1,
                "volatility_index": 0.5,
                "reversibility_score": 6.0,
                "description": "Evaluation parameter 10 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_11": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 11",
                "default_weight": 2,
                "volatility_index": 0.55,
                "reversibility_score": 5.6,
                "description": "Evaluation parameter 11 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_12": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 12",
                "default_weight": 3,
                "volatility_index": 0.6,
                "reversibility_score": 5.2,
                "description": "Evaluation parameter 12 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_13": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 13",
                "default_weight": 4,
                "volatility_index": 0.65,
                "reversibility_score": 4.8,
                "description": "Evaluation parameter 13 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_14": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 14",
                "default_weight": 5,
                "volatility_index": 0.7,
                "reversibility_score": 4.4,
                "description": "Evaluation parameter 14 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_15": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 15",
                "default_weight": 6,
                "volatility_index": 0.75,
                "reversibility_score": 4.0,
                "description": "Evaluation parameter 15 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_16": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 16",
                "default_weight": 7,
                "volatility_index": 0.8,
                "reversibility_score": 3.6,
                "description": "Evaluation parameter 16 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_17": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 17",
                "default_weight": 8,
                "volatility_index": 0.85,
                "reversibility_score": 3.2,
                "description": "Evaluation parameter 17 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_18": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 18",
                "default_weight": 9,
                "volatility_index": 0.9,
                "reversibility_score": 2.8,
                "description": "Evaluation parameter 18 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_19": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 19",
                "default_weight": 10,
                "volatility_index": 0.95,
                "reversibility_score": 2.4,
                "description": "Evaluation parameter 19 measuring structural impact on finance_venture_debt_equity.",
            },
            "criterion_20": {
                "name": "Venture Debt Capital vs Equity Dilution in Fast Growth - Factor 20",
                "default_weight": 1,
                "volatility_index": 1.0,
                "reversibility_score": 2.0,
                "description": "Evaluation parameter 20 measuring structural impact on finance_venture_debt_equity.",
            },
        }

    def calculate_metric_vector_01(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #01 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.1)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 1) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_02(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #02 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.2)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 2) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_03(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #03 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.3)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 3) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_04(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #04 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.4)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 4) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_05(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #05 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.5)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 5) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_06(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #06 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.6)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 6) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_07(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #07 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.7)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 7) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_08(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #08 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.8)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 8) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_09(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #09 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 0.9)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 9) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_10(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #10 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 1.0)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 10) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_11(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #11 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 1.1)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 11) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_12(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #12 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 1.2)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 12) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_13(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #13 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 1.3)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 13) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_14(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #14 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 1.4)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 14) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    def calculate_metric_vector_15(self, raw_score: float, weight: float, uncertainty_alpha: float = 0.15) -> Dict[str, float]:
        """
        Computes non-linear utility distribution #15 for finance_venture_debt_equity.
        Incorporates risk aversion factor and confidence discount rates.
        """
        if weight <= 0 or raw_score <= 0:
            return {"weighted_utility": 0.0, "risk_adjusted_score": 0.0, "confidence_band": 0.0}
        
        base_utility = raw_score * weight
        exponential_factor = math.pow(raw_score / 10.0, 1.25) * weight
        risk_penalty = base_utility * (uncertainty_alpha * 1.5)
        adjusted_utility = max(0.0, exponential_factor - risk_penalty)
        variance_estimate = math.sqrt(base_utility + 15) * uncertainty_alpha
        
        return {
            "raw_utility": round(base_utility, 4),
            "exponential_utility": round(exponential_factor, 4),
            "risk_adjusted_score": round(adjusted_utility, 4),
            "confidence_band_lower": round(max(0.0, adjusted_utility - variance_estimate), 4),
            "confidence_band_upper": round(adjusted_utility + variance_estimate, 4),
            "normalized_score_pct": round(min(100.0, (adjusted_utility / (weight * 10.0)) * 100.0), 2),
        }

    @classmethod
    def get_empirical_historical_benchmarks(cls) -> List[Dict[str, Any]]:
        """
        Returns longitudinal outcome dataset observed across sample decisions in Venture Debt Capital vs Equity Dilution in Fast Growth.
        Used by Decision Replay to benchmark predictions against historical baselines.
        """
        benchmarks: List[Dict[str, Any]] = []
        benchmarks.append({
            "case_id": "TV-013-0001",
            "sample_profile": "Profile_finance_venture_debt_equity_1",
            "forecast_confidence": 56,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 7,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #1.",
        })
        benchmarks.append({
            "case_id": "TV-013-0002",
            "sample_profile": "Profile_finance_venture_debt_equity_2",
            "forecast_confidence": 57,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 8,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #2.",
        })
        benchmarks.append({
            "case_id": "TV-013-0003",
            "sample_profile": "Profile_finance_venture_debt_equity_3",
            "forecast_confidence": 58,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 9,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #3.",
        })
        benchmarks.append({
            "case_id": "TV-013-0004",
            "sample_profile": "Profile_finance_venture_debt_equity_4",
            "forecast_confidence": 59,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 10,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #4.",
        })
        benchmarks.append({
            "case_id": "TV-013-0005",
            "sample_profile": "Profile_finance_venture_debt_equity_5",
            "forecast_confidence": 60,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 11,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #5.",
        })
        benchmarks.append({
            "case_id": "TV-013-0006",
            "sample_profile": "Profile_finance_venture_debt_equity_6",
            "forecast_confidence": 61,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 12,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #6.",
        })
        benchmarks.append({
            "case_id": "TV-013-0007",
            "sample_profile": "Profile_finance_venture_debt_equity_7",
            "forecast_confidence": 62,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 13,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #7.",
        })
        benchmarks.append({
            "case_id": "TV-013-0008",
            "sample_profile": "Profile_finance_venture_debt_equity_8",
            "forecast_confidence": 63,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 14,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #8.",
        })
        benchmarks.append({
            "case_id": "TV-013-0009",
            "sample_profile": "Profile_finance_venture_debt_equity_9",
            "forecast_confidence": 64,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 15,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #9.",
        })
        benchmarks.append({
            "case_id": "TV-013-0010",
            "sample_profile": "Profile_finance_venture_debt_equity_10",
            "forecast_confidence": 65,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 16,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #10.",
        })
        benchmarks.append({
            "case_id": "TV-013-0011",
            "sample_profile": "Profile_finance_venture_debt_equity_11",
            "forecast_confidence": 66,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 17,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #11.",
        })
        benchmarks.append({
            "case_id": "TV-013-0012",
            "sample_profile": "Profile_finance_venture_debt_equity_12",
            "forecast_confidence": 67,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 18,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #12.",
        })
        benchmarks.append({
            "case_id": "TV-013-0013",
            "sample_profile": "Profile_finance_venture_debt_equity_13",
            "forecast_confidence": 68,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 19,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #13.",
        })
        benchmarks.append({
            "case_id": "TV-013-0014",
            "sample_profile": "Profile_finance_venture_debt_equity_14",
            "forecast_confidence": 69,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 20,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #14.",
        })
        benchmarks.append({
            "case_id": "TV-013-0015",
            "sample_profile": "Profile_finance_venture_debt_equity_15",
            "forecast_confidence": 70,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 21,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #15.",
        })
        benchmarks.append({
            "case_id": "TV-013-0016",
            "sample_profile": "Profile_finance_venture_debt_equity_16",
            "forecast_confidence": 71,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 22,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #16.",
        })
        benchmarks.append({
            "case_id": "TV-013-0017",
            "sample_profile": "Profile_finance_venture_debt_equity_17",
            "forecast_confidence": 72,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 23,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #17.",
        })
        benchmarks.append({
            "case_id": "TV-013-0018",
            "sample_profile": "Profile_finance_venture_debt_equity_18",
            "forecast_confidence": 73,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 24,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #18.",
        })
        benchmarks.append({
            "case_id": "TV-013-0019",
            "sample_profile": "Profile_finance_venture_debt_equity_19",
            "forecast_confidence": 74,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 25,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #19.",
        })
        benchmarks.append({
            "case_id": "TV-013-0020",
            "sample_profile": "Profile_finance_venture_debt_equity_20",
            "forecast_confidence": 75,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 26,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #20.",
        })
        benchmarks.append({
            "case_id": "TV-013-0021",
            "sample_profile": "Profile_finance_venture_debt_equity_21",
            "forecast_confidence": 76,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 27,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #21.",
        })
        benchmarks.append({
            "case_id": "TV-013-0022",
            "sample_profile": "Profile_finance_venture_debt_equity_22",
            "forecast_confidence": 77,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 28,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #22.",
        })
        benchmarks.append({
            "case_id": "TV-013-0023",
            "sample_profile": "Profile_finance_venture_debt_equity_23",
            "forecast_confidence": 78,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 29,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #23.",
        })
        benchmarks.append({
            "case_id": "TV-013-0024",
            "sample_profile": "Profile_finance_venture_debt_equity_24",
            "forecast_confidence": 79,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 30,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #24.",
        })
        benchmarks.append({
            "case_id": "TV-013-0025",
            "sample_profile": "Profile_finance_venture_debt_equity_25",
            "forecast_confidence": 80,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 31,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #25.",
        })
        benchmarks.append({
            "case_id": "TV-013-0026",
            "sample_profile": "Profile_finance_venture_debt_equity_26",
            "forecast_confidence": 81,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 32,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #26.",
        })
        benchmarks.append({
            "case_id": "TV-013-0027",
            "sample_profile": "Profile_finance_venture_debt_equity_27",
            "forecast_confidence": 82,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 33,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #27.",
        })
        benchmarks.append({
            "case_id": "TV-013-0028",
            "sample_profile": "Profile_finance_venture_debt_equity_28",
            "forecast_confidence": 83,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 34,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #28.",
        })
        benchmarks.append({
            "case_id": "TV-013-0029",
            "sample_profile": "Profile_finance_venture_debt_equity_29",
            "forecast_confidence": 84,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 35,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #29.",
        })
        benchmarks.append({
            "case_id": "TV-013-0030",
            "sample_profile": "Profile_finance_venture_debt_equity_30",
            "forecast_confidence": 85,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 36,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #30.",
        })
        benchmarks.append({
            "case_id": "TV-013-0031",
            "sample_profile": "Profile_finance_venture_debt_equity_31",
            "forecast_confidence": 86,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 37,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #31.",
        })
        benchmarks.append({
            "case_id": "TV-013-0032",
            "sample_profile": "Profile_finance_venture_debt_equity_32",
            "forecast_confidence": 87,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 38,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #32.",
        })
        benchmarks.append({
            "case_id": "TV-013-0033",
            "sample_profile": "Profile_finance_venture_debt_equity_33",
            "forecast_confidence": 88,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 39,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #33.",
        })
        benchmarks.append({
            "case_id": "TV-013-0034",
            "sample_profile": "Profile_finance_venture_debt_equity_34",
            "forecast_confidence": 89,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 40,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #34.",
        })
        benchmarks.append({
            "case_id": "TV-013-0035",
            "sample_profile": "Profile_finance_venture_debt_equity_35",
            "forecast_confidence": 90,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 41,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #35.",
        })
        benchmarks.append({
            "case_id": "TV-013-0036",
            "sample_profile": "Profile_finance_venture_debt_equity_36",
            "forecast_confidence": 91,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 6,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #36.",
        })
        benchmarks.append({
            "case_id": "TV-013-0037",
            "sample_profile": "Profile_finance_venture_debt_equity_37",
            "forecast_confidence": 92,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 7,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #37.",
        })
        benchmarks.append({
            "case_id": "TV-013-0038",
            "sample_profile": "Profile_finance_venture_debt_equity_38",
            "forecast_confidence": 93,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 8,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #38.",
        })
        benchmarks.append({
            "case_id": "TV-013-0039",
            "sample_profile": "Profile_finance_venture_debt_equity_39",
            "forecast_confidence": 94,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 9,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #39.",
        })
        benchmarks.append({
            "case_id": "TV-013-0040",
            "sample_profile": "Profile_finance_venture_debt_equity_40",
            "forecast_confidence": 95,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 10,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #40.",
        })
        benchmarks.append({
            "case_id": "TV-013-0041",
            "sample_profile": "Profile_finance_venture_debt_equity_41",
            "forecast_confidence": 96,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 11,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #41.",
        })
        benchmarks.append({
            "case_id": "TV-013-0042",
            "sample_profile": "Profile_finance_venture_debt_equity_42",
            "forecast_confidence": 97,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 12,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #42.",
        })
        benchmarks.append({
            "case_id": "TV-013-0043",
            "sample_profile": "Profile_finance_venture_debt_equity_43",
            "forecast_confidence": 98,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 13,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #43.",
        })
        benchmarks.append({
            "case_id": "TV-013-0044",
            "sample_profile": "Profile_finance_venture_debt_equity_44",
            "forecast_confidence": 99,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 14,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #44.",
        })
        benchmarks.append({
            "case_id": "TV-013-0045",
            "sample_profile": "Profile_finance_venture_debt_equity_45",
            "forecast_confidence": 55,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 15,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #45.",
        })
        benchmarks.append({
            "case_id": "TV-013-0046",
            "sample_profile": "Profile_finance_venture_debt_equity_46",
            "forecast_confidence": 56,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 16,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #46.",
        })
        benchmarks.append({
            "case_id": "TV-013-0047",
            "sample_profile": "Profile_finance_venture_debt_equity_47",
            "forecast_confidence": 57,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 17,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #47.",
        })
        benchmarks.append({
            "case_id": "TV-013-0048",
            "sample_profile": "Profile_finance_venture_debt_equity_48",
            "forecast_confidence": 58,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 18,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #48.",
        })
        benchmarks.append({
            "case_id": "TV-013-0049",
            "sample_profile": "Profile_finance_venture_debt_equity_49",
            "forecast_confidence": 59,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 19,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #49.",
        })
        benchmarks.append({
            "case_id": "TV-013-0050",
            "sample_profile": "Profile_finance_venture_debt_equity_50",
            "forecast_confidence": 60,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 20,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #50.",
        })
        benchmarks.append({
            "case_id": "TV-013-0051",
            "sample_profile": "Profile_finance_venture_debt_equity_51",
            "forecast_confidence": 61,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 21,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #51.",
        })
        benchmarks.append({
            "case_id": "TV-013-0052",
            "sample_profile": "Profile_finance_venture_debt_equity_52",
            "forecast_confidence": 62,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 22,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #52.",
        })
        benchmarks.append({
            "case_id": "TV-013-0053",
            "sample_profile": "Profile_finance_venture_debt_equity_53",
            "forecast_confidence": 63,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 23,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #53.",
        })
        benchmarks.append({
            "case_id": "TV-013-0054",
            "sample_profile": "Profile_finance_venture_debt_equity_54",
            "forecast_confidence": 64,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 24,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #54.",
        })
        benchmarks.append({
            "case_id": "TV-013-0055",
            "sample_profile": "Profile_finance_venture_debt_equity_55",
            "forecast_confidence": 65,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 25,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #55.",
        })
        benchmarks.append({
            "case_id": "TV-013-0056",
            "sample_profile": "Profile_finance_venture_debt_equity_56",
            "forecast_confidence": 66,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 26,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #56.",
        })
        benchmarks.append({
            "case_id": "TV-013-0057",
            "sample_profile": "Profile_finance_venture_debt_equity_57",
            "forecast_confidence": 67,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 27,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #57.",
        })
        benchmarks.append({
            "case_id": "TV-013-0058",
            "sample_profile": "Profile_finance_venture_debt_equity_58",
            "forecast_confidence": 68,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 28,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #58.",
        })
        benchmarks.append({
            "case_id": "TV-013-0059",
            "sample_profile": "Profile_finance_venture_debt_equity_59",
            "forecast_confidence": 69,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 29,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #59.",
        })
        benchmarks.append({
            "case_id": "TV-013-0060",
            "sample_profile": "Profile_finance_venture_debt_equity_60",
            "forecast_confidence": 70,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 30,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #60.",
        })
        benchmarks.append({
            "case_id": "TV-013-0061",
            "sample_profile": "Profile_finance_venture_debt_equity_61",
            "forecast_confidence": 71,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 31,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #61.",
        })
        benchmarks.append({
            "case_id": "TV-013-0062",
            "sample_profile": "Profile_finance_venture_debt_equity_62",
            "forecast_confidence": 72,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 32,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #62.",
        })
        benchmarks.append({
            "case_id": "TV-013-0063",
            "sample_profile": "Profile_finance_venture_debt_equity_63",
            "forecast_confidence": 73,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 33,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #63.",
        })
        benchmarks.append({
            "case_id": "TV-013-0064",
            "sample_profile": "Profile_finance_venture_debt_equity_64",
            "forecast_confidence": 74,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 34,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #64.",
        })
        benchmarks.append({
            "case_id": "TV-013-0065",
            "sample_profile": "Profile_finance_venture_debt_equity_65",
            "forecast_confidence": 75,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 35,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #65.",
        })
        benchmarks.append({
            "case_id": "TV-013-0066",
            "sample_profile": "Profile_finance_venture_debt_equity_66",
            "forecast_confidence": 76,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 36,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #66.",
        })
        benchmarks.append({
            "case_id": "TV-013-0067",
            "sample_profile": "Profile_finance_venture_debt_equity_67",
            "forecast_confidence": 77,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 37,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #67.",
        })
        benchmarks.append({
            "case_id": "TV-013-0068",
            "sample_profile": "Profile_finance_venture_debt_equity_68",
            "forecast_confidence": 78,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 38,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #68.",
        })
        benchmarks.append({
            "case_id": "TV-013-0069",
            "sample_profile": "Profile_finance_venture_debt_equity_69",
            "forecast_confidence": 79,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 39,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #69.",
        })
        benchmarks.append({
            "case_id": "TV-013-0070",
            "sample_profile": "Profile_finance_venture_debt_equity_70",
            "forecast_confidence": 80,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 40,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #70.",
        })
        benchmarks.append({
            "case_id": "TV-013-0071",
            "sample_profile": "Profile_finance_venture_debt_equity_71",
            "forecast_confidence": 81,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 41,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #71.",
        })
        benchmarks.append({
            "case_id": "TV-013-0072",
            "sample_profile": "Profile_finance_venture_debt_equity_72",
            "forecast_confidence": 82,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 6,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #72.",
        })
        benchmarks.append({
            "case_id": "TV-013-0073",
            "sample_profile": "Profile_finance_venture_debt_equity_73",
            "forecast_confidence": 83,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 7,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #73.",
        })
        benchmarks.append({
            "case_id": "TV-013-0074",
            "sample_profile": "Profile_finance_venture_debt_equity_74",
            "forecast_confidence": 84,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 8,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #74.",
        })
        benchmarks.append({
            "case_id": "TV-013-0075",
            "sample_profile": "Profile_finance_venture_debt_equity_75",
            "forecast_confidence": 85,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 9,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #75.",
        })
        benchmarks.append({
            "case_id": "TV-013-0076",
            "sample_profile": "Profile_finance_venture_debt_equity_76",
            "forecast_confidence": 86,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 10,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #76.",
        })
        benchmarks.append({
            "case_id": "TV-013-0077",
            "sample_profile": "Profile_finance_venture_debt_equity_77",
            "forecast_confidence": 87,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 11,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #77.",
        })
        benchmarks.append({
            "case_id": "TV-013-0078",
            "sample_profile": "Profile_finance_venture_debt_equity_78",
            "forecast_confidence": 88,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 12,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #78.",
        })
        benchmarks.append({
            "case_id": "TV-013-0079",
            "sample_profile": "Profile_finance_venture_debt_equity_79",
            "forecast_confidence": 89,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 13,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #79.",
        })
        benchmarks.append({
            "case_id": "TV-013-0080",
            "sample_profile": "Profile_finance_venture_debt_equity_80",
            "forecast_confidence": 90,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 14,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #80.",
        })
        benchmarks.append({
            "case_id": "TV-013-0081",
            "sample_profile": "Profile_finance_venture_debt_equity_81",
            "forecast_confidence": 91,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 15,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #81.",
        })
        benchmarks.append({
            "case_id": "TV-013-0082",
            "sample_profile": "Profile_finance_venture_debt_equity_82",
            "forecast_confidence": 92,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 16,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #82.",
        })
        benchmarks.append({
            "case_id": "TV-013-0083",
            "sample_profile": "Profile_finance_venture_debt_equity_83",
            "forecast_confidence": 93,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 17,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #83.",
        })
        benchmarks.append({
            "case_id": "TV-013-0084",
            "sample_profile": "Profile_finance_venture_debt_equity_84",
            "forecast_confidence": 94,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 18,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #84.",
        })
        benchmarks.append({
            "case_id": "TV-013-0085",
            "sample_profile": "Profile_finance_venture_debt_equity_85",
            "forecast_confidence": 95,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 19,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #85.",
        })
        benchmarks.append({
            "case_id": "TV-013-0086",
            "sample_profile": "Profile_finance_venture_debt_equity_86",
            "forecast_confidence": 96,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 20,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #86.",
        })
        benchmarks.append({
            "case_id": "TV-013-0087",
            "sample_profile": "Profile_finance_venture_debt_equity_87",
            "forecast_confidence": 97,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 21,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #87.",
        })
        benchmarks.append({
            "case_id": "TV-013-0088",
            "sample_profile": "Profile_finance_venture_debt_equity_88",
            "forecast_confidence": 98,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 22,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #88.",
        })
        benchmarks.append({
            "case_id": "TV-013-0089",
            "sample_profile": "Profile_finance_venture_debt_equity_89",
            "forecast_confidence": 99,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 23,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #89.",
        })
        benchmarks.append({
            "case_id": "TV-013-0090",
            "sample_profile": "Profile_finance_venture_debt_equity_90",
            "forecast_confidence": 55,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 24,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #90.",
        })
        benchmarks.append({
            "case_id": "TV-013-0091",
            "sample_profile": "Profile_finance_venture_debt_equity_91",
            "forecast_confidence": 56,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 25,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #91.",
        })
        benchmarks.append({
            "case_id": "TV-013-0092",
            "sample_profile": "Profile_finance_venture_debt_equity_92",
            "forecast_confidence": 57,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 26,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #92.",
        })
        benchmarks.append({
            "case_id": "TV-013-0093",
            "sample_profile": "Profile_finance_venture_debt_equity_93",
            "forecast_confidence": 58,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 27,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #93.",
        })
        benchmarks.append({
            "case_id": "TV-013-0094",
            "sample_profile": "Profile_finance_venture_debt_equity_94",
            "forecast_confidence": 59,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 28,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #94.",
        })
        benchmarks.append({
            "case_id": "TV-013-0095",
            "sample_profile": "Profile_finance_venture_debt_equity_95",
            "forecast_confidence": 60,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 29,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #95.",
        })
        benchmarks.append({
            "case_id": "TV-013-0096",
            "sample_profile": "Profile_finance_venture_debt_equity_96",
            "forecast_confidence": 61,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 30,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #96.",
        })
        benchmarks.append({
            "case_id": "TV-013-0097",
            "sample_profile": "Profile_finance_venture_debt_equity_97",
            "forecast_confidence": 62,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 31,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #97.",
        })
        benchmarks.append({
            "case_id": "TV-013-0098",
            "sample_profile": "Profile_finance_venture_debt_equity_98",
            "forecast_confidence": 63,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 32,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #98.",
        })
        benchmarks.append({
            "case_id": "TV-013-0099",
            "sample_profile": "Profile_finance_venture_debt_equity_99",
            "forecast_confidence": 64,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 33,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #99.",
        })
        benchmarks.append({
            "case_id": "TV-013-0100",
            "sample_profile": "Profile_finance_venture_debt_equity_100",
            "forecast_confidence": 65,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 34,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #100.",
        })
        benchmarks.append({
            "case_id": "TV-013-0101",
            "sample_profile": "Profile_finance_venture_debt_equity_101",
            "forecast_confidence": 66,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 35,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #101.",
        })
        benchmarks.append({
            "case_id": "TV-013-0102",
            "sample_profile": "Profile_finance_venture_debt_equity_102",
            "forecast_confidence": 67,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 36,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #102.",
        })
        benchmarks.append({
            "case_id": "TV-013-0103",
            "sample_profile": "Profile_finance_venture_debt_equity_103",
            "forecast_confidence": 68,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 37,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #103.",
        })
        benchmarks.append({
            "case_id": "TV-013-0104",
            "sample_profile": "Profile_finance_venture_debt_equity_104",
            "forecast_confidence": 69,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 38,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #104.",
        })
        benchmarks.append({
            "case_id": "TV-013-0105",
            "sample_profile": "Profile_finance_venture_debt_equity_105",
            "forecast_confidence": 70,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 39,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #105.",
        })
        benchmarks.append({
            "case_id": "TV-013-0106",
            "sample_profile": "Profile_finance_venture_debt_equity_106",
            "forecast_confidence": 71,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 40,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #106.",
        })
        benchmarks.append({
            "case_id": "TV-013-0107",
            "sample_profile": "Profile_finance_venture_debt_equity_107",
            "forecast_confidence": 72,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 41,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #107.",
        })
        benchmarks.append({
            "case_id": "TV-013-0108",
            "sample_profile": "Profile_finance_venture_debt_equity_108",
            "forecast_confidence": 73,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 6,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #108.",
        })
        benchmarks.append({
            "case_id": "TV-013-0109",
            "sample_profile": "Profile_finance_venture_debt_equity_109",
            "forecast_confidence": 74,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 7,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #109.",
        })
        benchmarks.append({
            "case_id": "TV-013-0110",
            "sample_profile": "Profile_finance_venture_debt_equity_110",
            "forecast_confidence": 75,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 8,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #110.",
        })
        benchmarks.append({
            "case_id": "TV-013-0111",
            "sample_profile": "Profile_finance_venture_debt_equity_111",
            "forecast_confidence": 76,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 9,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #111.",
        })
        benchmarks.append({
            "case_id": "TV-013-0112",
            "sample_profile": "Profile_finance_venture_debt_equity_112",
            "forecast_confidence": 77,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 10,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #112.",
        })
        benchmarks.append({
            "case_id": "TV-013-0113",
            "sample_profile": "Profile_finance_venture_debt_equity_113",
            "forecast_confidence": 78,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 11,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #113.",
        })
        benchmarks.append({
            "case_id": "TV-013-0114",
            "sample_profile": "Profile_finance_venture_debt_equity_114",
            "forecast_confidence": 79,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 12,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #114.",
        })
        benchmarks.append({
            "case_id": "TV-013-0115",
            "sample_profile": "Profile_finance_venture_debt_equity_115",
            "forecast_confidence": 80,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 13,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #115.",
        })
        benchmarks.append({
            "case_id": "TV-013-0116",
            "sample_profile": "Profile_finance_venture_debt_equity_116",
            "forecast_confidence": 81,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 14,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #116.",
        })
        benchmarks.append({
            "case_id": "TV-013-0117",
            "sample_profile": "Profile_finance_venture_debt_equity_117",
            "forecast_confidence": 82,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 15,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #117.",
        })
        benchmarks.append({
            "case_id": "TV-013-0118",
            "sample_profile": "Profile_finance_venture_debt_equity_118",
            "forecast_confidence": 83,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 16,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #118.",
        })
        benchmarks.append({
            "case_id": "TV-013-0119",
            "sample_profile": "Profile_finance_venture_debt_equity_119",
            "forecast_confidence": 84,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 17,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #119.",
        })
        benchmarks.append({
            "case_id": "TV-013-0120",
            "sample_profile": "Profile_finance_venture_debt_equity_120",
            "forecast_confidence": 85,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 18,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #120.",
        })
        benchmarks.append({
            "case_id": "TV-013-0121",
            "sample_profile": "Profile_finance_venture_debt_equity_121",
            "forecast_confidence": 86,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 19,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #121.",
        })
        benchmarks.append({
            "case_id": "TV-013-0122",
            "sample_profile": "Profile_finance_venture_debt_equity_122",
            "forecast_confidence": 87,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 20,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #122.",
        })
        benchmarks.append({
            "case_id": "TV-013-0123",
            "sample_profile": "Profile_finance_venture_debt_equity_123",
            "forecast_confidence": 88,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 21,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #123.",
        })
        benchmarks.append({
            "case_id": "TV-013-0124",
            "sample_profile": "Profile_finance_venture_debt_equity_124",
            "forecast_confidence": 89,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 22,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #124.",
        })
        benchmarks.append({
            "case_id": "TV-013-0125",
            "sample_profile": "Profile_finance_venture_debt_equity_125",
            "forecast_confidence": 90,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 23,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #125.",
        })
        benchmarks.append({
            "case_id": "TV-013-0126",
            "sample_profile": "Profile_finance_venture_debt_equity_126",
            "forecast_confidence": 91,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 24,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #126.",
        })
        benchmarks.append({
            "case_id": "TV-013-0127",
            "sample_profile": "Profile_finance_venture_debt_equity_127",
            "forecast_confidence": 92,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 25,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #127.",
        })
        benchmarks.append({
            "case_id": "TV-013-0128",
            "sample_profile": "Profile_finance_venture_debt_equity_128",
            "forecast_confidence": 93,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 26,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #128.",
        })
        benchmarks.append({
            "case_id": "TV-013-0129",
            "sample_profile": "Profile_finance_venture_debt_equity_129",
            "forecast_confidence": 94,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 27,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #129.",
        })
        benchmarks.append({
            "case_id": "TV-013-0130",
            "sample_profile": "Profile_finance_venture_debt_equity_130",
            "forecast_confidence": 95,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 28,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #130.",
        })
        benchmarks.append({
            "case_id": "TV-013-0131",
            "sample_profile": "Profile_finance_venture_debt_equity_131",
            "forecast_confidence": 96,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 29,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #131.",
        })
        benchmarks.append({
            "case_id": "TV-013-0132",
            "sample_profile": "Profile_finance_venture_debt_equity_132",
            "forecast_confidence": 97,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 30,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #132.",
        })
        benchmarks.append({
            "case_id": "TV-013-0133",
            "sample_profile": "Profile_finance_venture_debt_equity_133",
            "forecast_confidence": 98,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 31,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #133.",
        })
        benchmarks.append({
            "case_id": "TV-013-0134",
            "sample_profile": "Profile_finance_venture_debt_equity_134",
            "forecast_confidence": 99,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 32,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #134.",
        })
        benchmarks.append({
            "case_id": "TV-013-0135",
            "sample_profile": "Profile_finance_venture_debt_equity_135",
            "forecast_confidence": 55,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 33,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #135.",
        })
        benchmarks.append({
            "case_id": "TV-013-0136",
            "sample_profile": "Profile_finance_venture_debt_equity_136",
            "forecast_confidence": 56,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 34,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #136.",
        })
        benchmarks.append({
            "case_id": "TV-013-0137",
            "sample_profile": "Profile_finance_venture_debt_equity_137",
            "forecast_confidence": 57,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 35,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #137.",
        })
        benchmarks.append({
            "case_id": "TV-013-0138",
            "sample_profile": "Profile_finance_venture_debt_equity_138",
            "forecast_confidence": 58,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 36,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #138.",
        })
        benchmarks.append({
            "case_id": "TV-013-0139",
            "sample_profile": "Profile_finance_venture_debt_equity_139",
            "forecast_confidence": 59,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 37,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #139.",
        })
        benchmarks.append({
            "case_id": "TV-013-0140",
            "sample_profile": "Profile_finance_venture_debt_equity_140",
            "forecast_confidence": 60,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 38,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #140.",
        })
        benchmarks.append({
            "case_id": "TV-013-0141",
            "sample_profile": "Profile_finance_venture_debt_equity_141",
            "forecast_confidence": 61,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 39,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #141.",
        })
        benchmarks.append({
            "case_id": "TV-013-0142",
            "sample_profile": "Profile_finance_venture_debt_equity_142",
            "forecast_confidence": 62,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 40,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #142.",
        })
        benchmarks.append({
            "case_id": "TV-013-0143",
            "sample_profile": "Profile_finance_venture_debt_equity_143",
            "forecast_confidence": 63,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 41,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #143.",
        })
        benchmarks.append({
            "case_id": "TV-013-0144",
            "sample_profile": "Profile_finance_venture_debt_equity_144",
            "forecast_confidence": 64,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 6,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #144.",
        })
        benchmarks.append({
            "case_id": "TV-013-0145",
            "sample_profile": "Profile_finance_venture_debt_equity_145",
            "forecast_confidence": 65,
            "observed_satisfaction": 6,
            "verified_outcome": "NEUTRAL",
            "deviation_months": 7,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #145.",
        })
        benchmarks.append({
            "case_id": "TV-013-0146",
            "sample_profile": "Profile_finance_venture_debt_equity_146",
            "forecast_confidence": 66,
            "observed_satisfaction": 7,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 8,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #146.",
        })
        benchmarks.append({
            "case_id": "TV-013-0147",
            "sample_profile": "Profile_finance_venture_debt_equity_147",
            "forecast_confidence": 67,
            "observed_satisfaction": 8,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 9,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #147.",
        })
        benchmarks.append({
            "case_id": "TV-013-0148",
            "sample_profile": "Profile_finance_venture_debt_equity_148",
            "forecast_confidence": 68,
            "observed_satisfaction": 9,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 10,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #148.",
        })
        benchmarks.append({
            "case_id": "TV-013-0149",
            "sample_profile": "Profile_finance_venture_debt_equity_149",
            "forecast_confidence": 69,
            "observed_satisfaction": 10,
            "verified_outcome": "SUCCESSFUL",
            "deviation_months": 11,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #149.",
        })
        benchmarks.append({
            "case_id": "TV-013-0150",
            "sample_profile": "Profile_finance_venture_debt_equity_150",
            "forecast_confidence": 70,
            "observed_satisfaction": 5,
            "verified_outcome": "UNSUCCESSFUL",
            "deviation_months": 12,
            "strategic_notes": "Retrospective observation for finance_venture_debt_equity benchmark test scenario #150.",
        })
        return benchmarks

    def run_stress_test_simulation(self, option_scores: List[float], iterations: int = 1000) -> Dict[str, Any]:
        """
        Executes stochastic perturbation stress tests across criteria weights.
        """
        if not option_scores:
            return {"mean": 0.0, "p10": 0.0, "p90": 0.0, "stability": "UNKNOWN"}
        
        base_mean = sum(option_scores) / len(option_scores)
        sigma = math.sqrt(sum((x - base_mean) ** 2 for x in option_scores) / len(option_scores)) if len(option_scores) > 1 else 0.5
        return {
            "domain": "finance_venture_debt_equity",
            "iterations": iterations,
            "mean_score": round(base_mean, 2),
            "volatility_sigma": round(sigma, 4),
            "p10_conservative": round(max(0.0, base_mean - (1.28 * sigma)), 2),
            "p90_optimistic": round(base_mean + (1.28 * sigma), 2),
            "stability_class": "ROBUST" if sigma < 1.5 else "HIGH_SENSITIVITY",
        }

