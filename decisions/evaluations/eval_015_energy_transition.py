"""
TimeVault Decision Evaluation Matrix — Protocol #015
Domain: energy_transition
High-Fidelity Multi-Criteria Sensitivity Matrix and Utility Optimization.
"""
from typing import Dict, List, Any, Tuple
import math

class EvaluationMatrix_015:
    MATRIX_ID: int = 15
    DOMAIN: str = "energy_transition"

    def __init__(self):
        self.weights_cache = {}

    def compute_sensitivity_tipping_point_01(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #01 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 1))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 1,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_02(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #02 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 2))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 2,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_03(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #03 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 3))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 3,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_04(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #04 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 4))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 4,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_05(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #05 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 5))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 5,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_06(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #06 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 6))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 6,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_07(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #07 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 7))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 7,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_08(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #08 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 8))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 8,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_09(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #09 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 9))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 9,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_10(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #10 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 10))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 10,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_11(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #11 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 11))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 11,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_12(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #12 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 12))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 12,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_13(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #13 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 13))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 13,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_14(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #14 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 14))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 14,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_15(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #15 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 15))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 15,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_16(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #16 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 16))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 16,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_17(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #17 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 17))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 17,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_18(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #18 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 18))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 18,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_19(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #19 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 19))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 19,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_20(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #20 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 20))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 20,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_21(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #21 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 21))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 21,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_22(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #22 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 22))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 22,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_23(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #23 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 23))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 23,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_24(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #24 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 24))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 24,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    def compute_sensitivity_tipping_point_25(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #25 for sensitivity in energy_transition.
        Determines minimal weight perturbation required to invert option ranking.
        """
        if not factor_weights or not candidate_ratings:
            return {"tipping_delta": 0.0, "is_critical": False, "elasticity": 0.0}
        
        weight_total = sum(factor_weights.values())
        normalized_weights = {k: (v / weight_total) for k, v in factor_weights.items()}
        primary_score = sum(candidate_ratings) / len(candidate_ratings)
        elasticity = primary_score * (1.0 + (0.01 * 25))
        tipping_delta = round(abs(10.0 - primary_score) * 0.12, 4)
        
        return {
            "factor_index": 25,
            "elasticity_coefficient": round(elasticity, 4),
            "tipping_delta": tipping_delta,
            "is_critical": tipping_delta < 0.8,
            "robustness_index": round(1.0 - (tipping_delta / 10.0), 4),
        }

    @classmethod
    def get_benchmark_matrix_records(cls) -> List[Dict[str, Any]]:
        records = []
        records.append({
            "matrix_case": "CASE-EVAL-015-0001",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 1 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0002",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 2 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0003",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 3 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0004",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 4 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0005",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 5 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0006",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 6 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0007",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 7 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0008",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 8 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0009",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 9 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0010",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 10 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0011",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 11 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0012",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 12 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0013",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 13 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0014",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 14 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0015",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 15 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0016",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 16 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0017",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 17 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0018",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 18 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0019",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 19 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0020",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 20 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0021",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 21 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0022",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 22 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0023",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 23 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0024",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 24 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0025",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 25 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0026",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 26 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0027",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 27 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0028",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 28 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0029",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 29 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0030",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 30 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0031",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 31 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0032",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 32 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0033",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 33 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0034",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 34 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0035",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 35 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0036",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 36 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0037",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 37 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0038",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 38 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0039",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 39 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0040",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 40 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0041",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 41 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0042",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 42 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0043",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 43 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0044",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 44 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0045",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 45 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0046",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 46 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0047",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 47 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0048",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 48 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0049",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 49 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0050",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 50 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0051",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 51 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0052",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 52 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0053",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 53 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0054",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 54 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0055",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 55 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0056",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 56 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0057",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 57 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0058",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 58 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0059",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 59 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0060",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 60 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0061",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 61 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0062",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 62 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0063",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 63 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0064",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 64 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0065",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 65 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0066",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 66 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0067",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 67 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0068",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 68 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0069",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 69 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0070",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 70 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0071",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 71 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0072",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 72 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0073",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 73 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0074",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 74 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0075",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 75 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0076",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 76 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0077",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 77 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0078",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 78 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0079",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 79 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0080",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 80 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0081",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 81 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0082",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 82 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0083",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 83 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0084",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 84 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0085",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 85 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0086",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 86 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0087",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 87 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0088",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 88 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0089",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 89 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0090",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 90 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0091",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 91 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0092",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 92 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0093",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 93 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0094",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 94 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0095",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 95 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0096",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 96 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0097",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 97 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0098",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 98 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0099",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 99 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0100",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 100 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0101",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 101 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0102",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 102 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0103",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 103 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0104",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 104 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0105",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 105 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0106",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 106 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0107",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 107 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0108",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 108 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0109",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 109 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0110",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 110 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0111",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 111 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0112",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 112 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0113",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 113 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0114",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 114 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0115",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 115 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0116",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 116 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0117",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 117 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0118",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 118 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0119",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 119 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0120",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 120 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0121",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 121 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0122",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 122 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0123",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 123 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0124",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 124 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0125",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 125 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0126",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 126 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0127",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 127 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0128",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 128 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0129",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 129 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0130",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 130 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0131",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 131 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0132",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 132 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0133",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 133 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0134",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 134 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0135",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 135 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0136",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 136 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0137",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 137 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0138",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 138 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0139",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 139 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0140",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 140 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0141",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 141 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0142",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 142 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0143",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 143 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0144",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 144 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0145",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 145 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0146",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 146 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0147",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 147 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0148",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 148 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0149",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 149 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0150",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 150 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0151",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 151 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0152",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 152 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0153",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 153 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0154",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 154 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0155",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 155 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0156",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 156 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0157",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 157 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0158",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 158 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0159",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 159 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0160",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 160 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0161",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 161 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0162",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 162 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0163",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 163 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0164",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 164 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0165",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 165 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0166",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 166 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0167",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 167 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0168",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 168 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0169",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 169 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0170",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 170 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0171",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 171 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0172",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 172 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0173",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 173 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0174",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 174 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0175",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 175 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0176",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 176 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0177",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 177 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0178",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 178 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0179",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 179 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0180",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 180 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0181",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 181 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0182",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 182 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0183",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 183 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0184",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 184 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0185",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 185 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0186",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 186 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0187",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 187 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0188",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 188 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0189",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 189 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0190",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 190 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0191",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 191 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0192",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 192 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0193",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 193 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0194",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 194 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0195",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 195 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0196",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 196 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0197",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 197 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0198",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 198 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0199",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 199 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0200",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 200 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0201",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 201 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0202",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 202 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0203",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 203 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0204",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 204 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0205",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 205 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0206",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 206 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0207",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 207 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0208",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 208 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0209",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 209 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0210",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 210 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0211",
            "category": "energy_transition",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 211 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0212",
            "category": "energy_transition",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 212 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0213",
            "category": "energy_transition",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 213 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0214",
            "category": "energy_transition",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 214 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0215",
            "category": "energy_transition",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 215 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0216",
            "category": "energy_transition",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 216 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0217",
            "category": "energy_transition",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 217 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0218",
            "category": "energy_transition",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 218 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0219",
            "category": "energy_transition",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 219 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-015-0220",
            "category": "energy_transition",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 220 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        return records

