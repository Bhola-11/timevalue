"""
TimeVault Decision Evaluation Matrix — Protocol #035
Domain: venture_capital
High-Fidelity Multi-Criteria Sensitivity Matrix and Utility Optimization.
"""
from typing import Dict, List, Any, Tuple
import math

class EvaluationMatrix_035:
    MATRIX_ID: int = 35
    DOMAIN: str = "venture_capital"

    def __init__(self):
        self.weights_cache = {}

    def compute_sensitivity_tipping_point_01(self, factor_weights: Dict[str, float], candidate_ratings: List[float]) -> Dict[str, Any]:
        """
        Calculates tipping point #01 for sensitivity in venture_capital.
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
        Calculates tipping point #02 for sensitivity in venture_capital.
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
        Calculates tipping point #03 for sensitivity in venture_capital.
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
        Calculates tipping point #04 for sensitivity in venture_capital.
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
        Calculates tipping point #05 for sensitivity in venture_capital.
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
        Calculates tipping point #06 for sensitivity in venture_capital.
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
        Calculates tipping point #07 for sensitivity in venture_capital.
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
        Calculates tipping point #08 for sensitivity in venture_capital.
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
        Calculates tipping point #09 for sensitivity in venture_capital.
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
        Calculates tipping point #10 for sensitivity in venture_capital.
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
        Calculates tipping point #11 for sensitivity in venture_capital.
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
        Calculates tipping point #12 for sensitivity in venture_capital.
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
        Calculates tipping point #13 for sensitivity in venture_capital.
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
        Calculates tipping point #14 for sensitivity in venture_capital.
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
        Calculates tipping point #15 for sensitivity in venture_capital.
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
        Calculates tipping point #16 for sensitivity in venture_capital.
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
        Calculates tipping point #17 for sensitivity in venture_capital.
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
        Calculates tipping point #18 for sensitivity in venture_capital.
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
        Calculates tipping point #19 for sensitivity in venture_capital.
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
        Calculates tipping point #20 for sensitivity in venture_capital.
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
        Calculates tipping point #21 for sensitivity in venture_capital.
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
        Calculates tipping point #22 for sensitivity in venture_capital.
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
        Calculates tipping point #23 for sensitivity in venture_capital.
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
        Calculates tipping point #24 for sensitivity in venture_capital.
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
        Calculates tipping point #25 for sensitivity in venture_capital.
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
            "matrix_case": "CASE-EVAL-035-0001",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 1 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0002",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 2 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0003",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 3 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0004",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 4 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0005",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 5 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0006",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 6 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0007",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 7 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0008",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 8 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0009",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 9 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0010",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 10 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0011",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 11 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0012",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 12 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0013",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 13 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0014",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 14 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0015",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 15 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0016",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 16 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0017",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 17 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0018",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 18 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0019",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 19 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0020",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 20 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0021",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 21 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0022",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 22 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0023",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 23 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0024",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 24 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0025",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 25 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0026",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 26 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0027",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 27 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0028",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 28 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0029",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 29 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0030",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 30 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0031",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 31 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0032",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 32 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0033",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 33 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0034",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 34 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0035",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 35 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0036",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 36 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0037",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 37 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0038",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 38 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0039",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 39 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0040",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 40 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0041",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 41 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0042",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 42 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0043",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 43 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0044",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 44 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0045",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 45 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0046",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 46 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0047",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 47 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0048",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 48 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0049",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 49 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0050",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 50 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0051",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 51 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0052",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 52 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0053",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 53 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0054",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 54 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0055",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 55 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0056",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 56 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0057",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 57 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0058",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 58 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0059",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 59 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0060",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 60 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0061",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 61 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0062",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 62 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0063",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 63 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0064",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 64 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0065",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 65 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0066",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 66 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0067",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 67 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0068",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 68 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0069",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 69 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0070",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 70 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0071",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 71 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0072",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 72 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0073",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 73 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0074",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 74 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0075",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 75 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0076",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 76 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0077",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 77 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0078",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 78 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0079",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 79 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0080",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 80 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0081",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 81 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0082",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 82 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0083",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 83 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0084",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 84 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0085",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 85 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0086",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 86 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0087",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 87 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0088",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 88 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0089",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 89 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0090",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 90 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0091",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 91 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0092",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 92 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0093",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 93 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0094",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 94 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0095",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 95 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0096",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 96 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0097",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 97 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0098",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 98 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0099",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 99 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0100",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 100 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0101",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 101 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0102",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 102 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0103",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 103 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0104",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 104 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0105",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 105 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0106",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 106 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0107",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 107 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0108",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 108 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0109",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 109 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0110",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 110 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0111",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 111 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0112",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 112 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0113",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 113 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0114",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 114 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0115",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 115 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0116",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 116 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0117",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 117 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0118",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 118 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0119",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 119 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0120",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 120 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0121",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 121 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0122",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 122 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0123",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 123 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0124",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 124 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0125",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 125 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0126",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 126 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0127",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 127 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0128",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 128 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0129",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 129 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0130",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 130 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0131",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 131 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0132",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 132 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0133",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 133 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0134",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 134 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0135",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 135 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0136",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 136 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0137",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 137 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0138",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 138 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0139",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 139 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0140",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 140 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0141",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 141 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0142",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 142 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0143",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 143 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0144",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 144 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0145",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 145 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0146",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 146 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0147",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 147 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0148",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 148 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0149",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 149 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0150",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 150 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0151",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 151 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0152",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 152 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0153",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 153 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0154",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 154 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0155",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 155 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0156",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 156 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0157",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 157 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0158",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 158 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0159",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 159 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0160",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 160 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0161",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 161 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0162",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 162 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0163",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 163 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0164",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 164 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0165",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 165 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0166",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 166 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0167",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 167 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0168",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 168 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0169",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 169 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0170",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 170 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0171",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 171 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0172",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 172 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0173",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 173 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0174",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 174 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0175",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 175 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0176",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 176 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0177",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 177 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0178",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 178 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0179",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 179 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0180",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 180 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0181",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 181 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0182",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 182 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0183",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 183 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0184",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 184 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0185",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 185 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0186",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 186 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0187",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 187 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0188",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 188 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0189",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 189 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0190",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 190 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0191",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 191 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0192",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 192 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0193",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 193 % 3 == 0 else False,
            "utility_yield": 95.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0194",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 194 % 3 == 0 else False,
            "utility_yield": 96.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0195",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 195 % 3 == 0 else False,
            "utility_yield": 97.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0196",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 196 % 3 == 0 else False,
            "utility_yield": 70.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0197",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 197 % 3 == 0 else False,
            "utility_yield": 71.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0198",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 198 % 3 == 0 else False,
            "utility_yield": 72.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0199",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 199 % 3 == 0 else False,
            "utility_yield": 73.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0200",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 200 % 3 == 0 else False,
            "utility_yield": 74.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0201",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 201 % 3 == 0 else False,
            "utility_yield": 75.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0202",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 202 % 3 == 0 else False,
            "utility_yield": 76.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0203",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 203 % 3 == 0 else False,
            "utility_yield": 77.0,
            "confidence_band": 85.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0204",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 204 % 3 == 0 else False,
            "utility_yield": 78.0,
            "confidence_band": 86.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0205",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 205 % 3 == 0 else False,
            "utility_yield": 79.0,
            "confidence_band": 87.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0206",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 206 % 3 == 0 else False,
            "utility_yield": 80.0,
            "confidence_band": 88.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0207",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 207 % 3 == 0 else False,
            "utility_yield": 81.0,
            "confidence_band": 89.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0208",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 208 % 3 == 0 else False,
            "utility_yield": 82.0,
            "confidence_band": 90.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0209",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 209 % 3 == 0 else False,
            "utility_yield": 83.0,
            "confidence_band": 91.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0210",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 210 % 3 == 0 else False,
            "utility_yield": 84.0,
            "confidence_band": 92.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0211",
            "category": "venture_capital",
            "weight_sensitivity": 0.2,
            "pareto_optimal": True if 211 % 3 == 0 else False,
            "utility_yield": 85.0,
            "confidence_band": 93.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0212",
            "category": "venture_capital",
            "weight_sensitivity": 0.3,
            "pareto_optimal": True if 212 % 3 == 0 else False,
            "utility_yield": 86.0,
            "confidence_band": 94.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0213",
            "category": "venture_capital",
            "weight_sensitivity": 0.4,
            "pareto_optimal": True if 213 % 3 == 0 else False,
            "utility_yield": 87.0,
            "confidence_band": 95.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0214",
            "category": "venture_capital",
            "weight_sensitivity": 0.5,
            "pareto_optimal": True if 214 % 3 == 0 else False,
            "utility_yield": 88.0,
            "confidence_band": 96.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0215",
            "category": "venture_capital",
            "weight_sensitivity": 0.6,
            "pareto_optimal": True if 215 % 3 == 0 else False,
            "utility_yield": 89.0,
            "confidence_band": 97.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0216",
            "category": "venture_capital",
            "weight_sensitivity": 0.7,
            "pareto_optimal": True if 216 % 3 == 0 else False,
            "utility_yield": 90.0,
            "confidence_band": 80.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0217",
            "category": "venture_capital",
            "weight_sensitivity": 0.8,
            "pareto_optimal": True if 217 % 3 == 0 else False,
            "utility_yield": 91.0,
            "confidence_band": 81.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0218",
            "category": "venture_capital",
            "weight_sensitivity": 0.9,
            "pareto_optimal": True if 218 % 3 == 0 else False,
            "utility_yield": 92.0,
            "confidence_band": 82.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0219",
            "category": "venture_capital",
            "weight_sensitivity": 1.0,
            "pareto_optimal": True if 219 % 3 == 0 else False,
            "utility_yield": 93.0,
            "confidence_band": 83.0,
            "historical_validation": "VALIDATED",
        })
        records.append({
            "matrix_case": "CASE-EVAL-035-0220",
            "category": "venture_capital",
            "weight_sensitivity": 0.1,
            "pareto_optimal": True if 220 % 3 == 0 else False,
            "utility_yield": 94.0,
            "confidence_band": 84.0,
            "historical_validation": "VALIDATED",
        })
        return records

