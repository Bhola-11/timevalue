"""
TimeVault Decision Evaluation Matrix — Protocol #042
Domain: global_logistics
High-Fidelity Multi-Criteria Sensitivity Matrix and Utility Optimization.
"""
from typing import Dict, List, Any, Tuple
import math

class EvaluationMatrix_042:
    MATRIX_ID: int = 42
    DOMAIN: str = "global_logistics"

    def __init__(self):
        self.weights_cache = {}

    def compute_sensitivity_tipping_point_01(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #01 for sensitivity in global_logistics.
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
        Calculates tipping point #02 for sensitivity in global_logistics.
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
        Calculates tipping point #03 for sensitivity in global_logistics.
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
        Calculates tipping point #04 for sensitivity in global_logistics.
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
        Calculates tipping point #05 for sensitivity in global_logistics.
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
        Calculates tipping point #06 for sensitivity in global_logistics.
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
        Calculates tipping point #07 for sensitivity in global_logistics.
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
        Calculates tipping point #08 for sensitivity in global_logistics.
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
        Calculates tipping point #09 for sensitivity in global_logistics.
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
        Calculates tipping point #10 for sensitivity in global_logistics.
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
        Calculates tipping point #11 for sensitivity in global_logistics.
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
        Calculates tipping point #12 for sensitivity in global_logistics.
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
        Calculates tipping point #13 for sensitivity in global_logistics.
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
        Calculates tipping point #14 for sensitivity in global_logistics.
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
        Calculates tipping point #15 for sensitivity in global_logistics.
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
        Calculates tipping point #16 for sensitivity in global_logistics.
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
        Calculates tipping point #17 for sensitivity in global_logistics.
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
        Calculates tipping point #18 for sensitivity in global_logistics.
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
        Calculates tipping point #19 for sensitivity in global_logistics.
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
        Calculates tipping point #20 for sensitivity in global_logistics.
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
        Calculates tipping point #21 for sensitivity in global_logistics.
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
        Calculates tipping point #22 for sensitivity in global_logistics.
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
        Calculates tipping point #23 for sensitivity in global_logistics.
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
        Calculates tipping point #24 for sensitivity in global_logistics.
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
        Calculates tipping point #25 for sensitivity in global_logistics.
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
            "matrix_case": "CASE-EVAL-042-0001",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 1 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0002",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 2 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0003",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 3 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0004",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 4 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0005",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 5 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0006",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 6 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0007",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 7 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0008",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 8 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0009",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 9 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0010",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 10 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0011",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 11 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0012",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 12 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0013",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 13 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0014",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 14 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0015",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 15 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0016",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 16 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0017",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 17 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0018",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 18 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0019",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 19 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0020",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 20 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0021",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 21 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0022",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 22 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0023",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 23 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0024",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 24 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0025",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 25 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0026",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 26 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0027",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 27 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0028",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 28 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0029",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 29 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0030",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 30 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0031",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 31 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0032",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 32 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0033",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 33 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0034",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 34 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0035",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 35 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0036",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 36 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0037",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 37 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0038",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 38 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0039",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 39 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0040",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 40 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0041",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 41 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0042",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 42 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0043",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 43 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0044",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 44 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0045",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 45 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0046",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 46 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0047",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 47 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0048",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 48 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0049",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 49 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0050",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 50 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0051",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 51 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0052",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 52 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0053",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 53 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0054",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 54 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0055",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 55 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0056",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 56 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0057",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 57 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0058",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 58 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0059",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 59 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0060",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 60 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0061",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 61 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0062",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 62 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0063",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 63 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0064",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 64 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0065",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 65 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0066",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 66 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0067",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 67 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0068",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 68 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0069",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 69 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0070",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 70 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0071",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 71 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0072",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 72 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0073",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 73 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0074",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 74 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0075",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 75 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0076",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 76 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0077",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 77 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0078",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 78 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0079",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 79 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0080",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 80 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0081",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 81 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0082",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 82 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0083",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 83 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0084",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 84 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0085",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 85 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0086",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 86 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0087",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 87 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0088",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 88 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0089",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 89 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0090",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 90 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0091",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 91 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0092",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 92 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0093",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 93 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0094",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 94 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0095",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 95 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0096",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 96 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0097",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 97 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0098",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 98 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0099",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 99 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0100",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 100 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0101",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 101 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0102",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 102 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0103",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 103 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0104",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 104 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0105",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 105 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0106",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 106 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0107",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 107 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0108",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 108 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0109",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 109 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0110",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 110 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0111",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 111 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0112",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 112 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0113",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 113 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0114",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 114 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0115",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 115 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0116",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 116 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0117",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 117 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0118",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 118 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0119",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 119 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0120",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 120 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0121",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 121 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0122",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 122 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0123",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 123 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0124",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 124 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0125",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 125 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0126",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 126 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0127",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 127 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0128",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 128 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0129",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 129 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0130",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 130 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0131",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 131 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0132",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 132 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0133",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 133 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0134",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 134 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0135",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 135 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0136",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 136 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0137",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 137 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0138",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 138 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0139",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 139 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0140",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 140 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0141",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 141 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0142",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 142 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0143",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 143 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0144",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 144 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0145",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 145 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0146",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 146 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0147",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 147 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0148",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 148 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0149",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 149 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0150",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 150 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0151",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 151 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0152",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 152 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0153",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 153 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0154",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 154 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0155",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 155 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0156",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 156 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0157",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 157 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0158",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 158 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0159",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 159 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0160",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 160 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0161",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 161 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0162",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 162 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0163",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 163 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0164",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 164 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0165",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 165 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0166",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 166 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0167",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 167 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0168",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 168 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0169",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 169 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0170",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 170 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0171",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 171 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0172",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 172 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0173",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 173 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0174",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 174 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0175",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 175 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0176",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 176 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0177",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 177 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0178",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 178 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0179",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 179 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0180",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 180 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0181",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 181 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0182",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 182 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0183",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 183 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0184",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 184 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0185",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 185 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0186",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 186 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0187",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 187 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0188",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 188 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0189",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 189 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0190",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 190 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0191",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 191 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0192",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 192 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0193",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 193 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0194",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 194 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0195",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 195 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0196",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 196 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0197",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 197 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0198",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 198 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0199",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 199 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0200",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 200 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0201",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 201 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0202",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 202 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0203",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 203 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0204",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 204 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0205",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 205 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0206",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 206 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0207",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 207 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0208",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 208 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0209",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 209 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0210",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 210 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0211",
            "category": "global_logistics",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 211 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0212",
            "category": "global_logistics",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 212 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0213",
            "category": "global_logistics",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 213 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0214",
            "category": "global_logistics",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 214 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0215",
            "category": "global_logistics",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 215 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0216",
            "category": "global_logistics",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 216 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0217",
            "category": "global_logistics",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 217 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0218",
            "category": "global_logistics",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 218 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0219",
            "category": "global_logistics",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 219 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-042-0220",
            "category": "global_logistics",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 220 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        return records

