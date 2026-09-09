"""
TimeVault Scoring and Analytical Engine (Service Layer)
Performs pure mathematical computations for Multi-Criteria Decision Analysis (MCDA),
option rankings, score normalizations, and outcome prediction replay analytics.
"""
from typing import Dict, Any, List
from .models import Decision, DecisionOption, DecisionFactor, FactorScore, DecisionOutcome, DecisionEvent


def calculate_decision_scores(decision: Decision) -> Dict[str, Any]:
    """
    Computes weighted scores, percentages, and ranks for all options in a decision.
    
    Formula:
      Weighted Score(Option) = SUM(Factor.weight * Score(Option, Factor))
      Max Score = SUM(Factor.weight * 10)
      Percentage = (Weighted Score / Max Score) * 100
      
    Returns a structured dictionary with option metrics, ranking, top candidate,
    and alignment with user's selected choice.
    """
    options = list(decision.options.all().prefetch_related('pros_cons'))
    factors = list(decision.factors.all())
    
    if not factors:
        total_weight = 0
        max_possible_score = 0
    else:
        total_weight = sum(f.weight for f in factors)
        max_possible_score = total_weight * 10

    # Pre-fetch factor scores into a lookup dict: (factor_id, option_id) -> score
    raw_scores = FactorScore.objects.filter(factor__decision=decision).select_related('factor', 'option')
    score_lookup = {(fs.factor_id, fs.option_id): fs.score for fs in raw_scores}

    option_results = []
    
    for opt in options:
        weighted_sum = 0
        factor_breakdown = []

        for f in factors:
            score_val = score_lookup.get((f.id, opt.id), 5)  # Default rating 5 if not yet scored
            weighted_val = f.weight * score_val
            weighted_sum += weighted_val
            factor_breakdown.append({
                'factor_id': f.id,
                'factor_name': f.name,
                'weight': f.weight,
                'score': score_val,
                'weighted_score': weighted_val,
            })

        percentage = round((weighted_sum / max_possible_score * 100), 1) if max_possible_score > 0 else 0.0

        pros = [pc.text for pc in opt.pros_cons.all() if pc.type == 'PRO']
        cons = [pc.text for pc in opt.pros_cons.all() if pc.type == 'CON']

        option_results.append({
            'option': opt,
            'id': opt.id,
            'title': opt.title,
            'description': opt.description,
            'weighted_sum': weighted_sum,
            'percentage': percentage,
            'factor_breakdown': factor_breakdown,
            'pros': pros,
            'cons': cons,
            'is_selected': decision.selected_option_id == opt.id,
        })

    # Sort options descending by percentage score
    option_results.sort(key=lambda x: x['percentage'], reverse=True)

    # Assign ranks
    for rank, item in enumerate(option_results, start=1):
        item['rank'] = rank

    highest_scoring = option_results[0] if option_results else None
    selected_result = next((item for item in option_results if item['is_selected']), None)

    score_difference = 0.0
    is_aligned = False
    if selected_result and highest_scoring:
        score_difference = round(selected_result['percentage'] - highest_scoring['percentage'], 1)
        is_aligned = (selected_result['id'] == highest_scoring['id'])

    return {
        'total_factors': len(factors),
        'total_options': len(options),
        'total_weight': total_weight,
        'max_possible_score': max_possible_score,
        'options': option_results,
        'highest_scoring': highest_scoring,
        'selected_result': selected_result,
        'score_difference': score_difference,
        'is_aligned': is_aligned,
    }


def analyze_decision_replay(decision: Decision) -> Dict[str, Any]:
    """
    Evaluates Decision Replay for completed or outcome-recorded decisions.
    Compares the original quantitative prediction against actual lived reality.
    """
    scores_data = calculate_decision_scores(decision)
    outcome = getattr(decision, 'outcome', None)

    if not outcome:
        return {
            'has_outcome': False,
            'scores_data': scores_data,
        }

    # Accuracy heuristic based on confidence and actual outcome
    # Confidence: 1-100%
    # Outcome: SUCCESSFUL, NEUTRAL, UNSUCCESSFUL
    # Satisfaction: 1-10
    conf = decision.confidence_score or 50
    satisfaction = outcome.satisfaction_score

    # Normalized accuracy evaluation
    # High accuracy:
    # 1. High confidence (>=70) + SUCCESSFUL + satisfaction >= 7
    # 2. Low confidence (<50) + UNSUCCESSFUL + satisfaction <= 4 (accurate risk foresight)
    # Low accuracy:
    # 1. High confidence (>=70) + UNSUCCESSFUL
    # 2. Low confidence (<40) + SUCCESSFUL (underestimated outcome)
    accuracy_label = "Moderate"
    accuracy_score = 70

    if conf >= 70 and outcome.outcome_status == 'SUCCESSFUL' and satisfaction >= 7:
        accuracy_label = "High"
        accuracy_score = 92
    elif conf >= 75 and outcome.outcome_status == 'UNSUCCESSFUL':
        accuracy_label = "Low (Overconfident)"
        accuracy_score = 35
    elif conf <= 40 and outcome.outcome_status == 'SUCCESSFUL':
        accuracy_label = "Low (Underestimated)"
        accuracy_score = 45
    elif conf <= 45 and outcome.outcome_status == 'UNSUCCESSFUL':
        accuracy_label = "High (Risk Foresight)"
        accuracy_score = 88
    elif outcome.outcome_status == 'NEUTRAL':
        accuracy_label = "Moderate"
        accuracy_score = 65

    return {
        'has_outcome': True,
        'scores_data': scores_data,
        'outcome': outcome,
        'confidence_score': conf,
        'satisfaction_score': satisfaction,
        'accuracy_label': accuracy_label,
        'accuracy_score': accuracy_score,
        'is_aligned': scores_data.get('is_aligned', False),
        'score_difference': scores_data.get('score_difference', 0.0),
    }


def record_timeline_event(decision: Decision, event_type: str, title: str, description: str = "") -> DecisionEvent:
    """
    Creates an immutable milestone record in the decision's timeline.
    """
    return DecisionEvent.objects.create(
        decision=decision,
        event_type=event_type,
        title=title,
        description=description,
    )
