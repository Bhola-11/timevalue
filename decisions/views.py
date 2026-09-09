"""
TimeVault Views (MVT Architecture)
Handles user authentication, dashboard analytics, decision lifecycle workflows,
scoring matrix updates, outcome evaluation, and retrospective Decision Replay.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count, Avg
from django.http import Http404

from .models import (
    Decision, DecisionOption, DecisionFactor, FactorScore,
    ProsCons, DecisionOutcome, DecisionEvent
)
from .forms import (
    UserRegistrationForm, DecisionBasicForm, FinalDecisionForm, OutcomeForm
)
from .services import (
    calculate_decision_scores, analyze_decision_replay, record_timeline_event
)


def register_view(request):
    """
    Handles user onboarding and initial session generation.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to TimeVault, {user.username}! Your decision vault is ready.")
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    """
    Terminates user session and redirects to login.
    """
    logout(request)
    messages.info(request, "You have been securely signed out.")
    return redirect('login')


@login_required
def dashboard_view(request):
    """
    Main Intelligence Dashboard: Aggregates decision metrics, status ratios,
    success rates, pending reminders, and recent records for the logged-in user.
    """
    user = request.user
    user_decisions = Decision.objects.filter(user=user)

    total_decisions = user_decisions.count()
    active_decisions = user_decisions.filter(status__in=['ACTIVE', 'DRAFT']).count()
    decided_decisions = user_decisions.filter(status='DECIDED').count()
    completed_decisions = user_decisions.filter(status='COMPLETED').count()
    
    # Decisions decided but awaiting real-world outcome
    outcome_pending = user_decisions.filter(status__in=['DECIDED', 'OUTCOME_PENDING']).exclude(status='COMPLETED').count()

    # Outcome statistics
    outcomes = DecisionOutcome.objects.filter(decision__user=user)
    total_outcomes = outcomes.count()
    successful_count = outcomes.filter(outcome_status='SUCCESSFUL').count()
    neutral_count = outcomes.filter(outcome_status='NEUTRAL').count()
    unsuccessful_count = outcomes.filter(outcome_status='UNSUCCESSFUL').count()

    success_rate = round((successful_count / total_outcomes * 100), 1) if total_outcomes > 0 else 0

    # Average confidence score across decided decisions
    avg_confidence = user_decisions.filter(confidence_score__isnull=False).aggregate(Avg('confidence_score'))['confidence_score__avg']
    avg_confidence = round(avg_confidence, 1) if avg_confidence else 0

    # Category breakdown
    category_counts = (
        user_decisions.values('category')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    recent_decisions = user_decisions.select_related('selected_option').prefetch_related('options')[:6]

    # Reminders: decisions with passed deadlines or awaiting outcome
    reminders = user_decisions.filter(status__in=['ACTIVE', 'DECIDED', 'OUTCOME_PENDING']).order_by('deadline')[:4]

    context = {
        'total_decisions': total_decisions,
        'active_decisions': active_decisions,
        'decided_decisions': decided_decisions,
        'completed_decisions': completed_decisions,
        'outcome_pending': outcome_pending,
        'successful_count': successful_count,
        'neutral_count': neutral_count,
        'unsuccessful_count': unsuccessful_count,
        'success_rate': success_rate,
        'avg_confidence': avg_confidence,
        'category_counts': category_counts,
        'recent_decisions': recent_decisions,
        'reminders': reminders,
    }
    return render(request, 'decisions/dashboard.html', context)


@login_required
def decision_list_view(request):
    """
    Search and filter index for all decisions belonging to the authenticated user.
    """
    decisions = Decision.objects.filter(user=request.user).select_related('selected_option')

    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    status = request.GET.get('status', '').strip()
    importance = request.GET.get('importance', '').strip()
    sort_by = request.GET.get('sort', '-updated_at').strip()

    if query:
        decisions = decisions.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if category:
        decisions = decisions.filter(category=category)
    if status:
        decisions = decisions.filter(status=status)
    if importance:
        decisions = decisions.filter(importance=importance)

    valid_sorts = {
        'newest': '-created_at',
        'oldest': 'created_at',
        'updated': '-updated_at',
        'deadline': 'deadline',
        'title': 'title',
    }
    decisions = decisions.order_by(valid_sorts.get(sort_by, '-updated_at'))

    context = {
        'decisions': decisions,
        'categories': Decision.CATEGORY_CHOICES,
        'statuses': Decision.STATUS_CHOICES,
        'importances': Decision.IMPORTANCE_CHOICES,
        'current_query': query,
        'current_category': category,
        'current_status': status,
        'current_importance': importance,
        'current_sort': sort_by,
        'total_count': decisions.count(),
    }
    return render(request, 'decisions/decision_list.html', context)


@login_required
def decision_create_view(request):
    """
    Step 1: Initialize basic decision metadata.
    Redirects to the interactive decision wizard.
    """
    if request.method == 'POST':
        form = DecisionBasicForm(request.POST)
        if form.is_valid():
            decision = form.save(commit=False)
            decision.user = request.user
            decision.status = 'ACTIVE'
            decision.save()

            record_timeline_event(
                decision,
                event_type='CREATED',
                title='Decision created',
                description=f"Initialized '{decision.title}' in category '{decision.get_category_display()}'."
            )
            messages.success(request, "Decision initialized! Now add your options and evaluation criteria.")
            return redirect('decision_wizard', pk=decision.pk)
    else:
        form = DecisionBasicForm()

    return render(request, 'decisions/decision_form.html', {'form': form, 'title': 'Create New Life Decision'})


@login_required
def decision_wizard_view(request, pk):
    """
    Multi-step interactive workspace:
    - Manage Options (Add/Remove)
    - Manage Factors & Weights (Add/Remove)
    - Score Matrix (Update Factor x Option ratings)
    - Add Pros/Cons
    - Finalize Decision choice, confidence, and reasoning.
    """
    decision = get_object_or_404(Decision, pk=pk, user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        # Action: Add Option
        if action == 'add_option':
            opt_title = request.POST.get('option_title', '').strip()
            opt_desc = request.POST.get('option_description', '').strip()
            if opt_title:
                next_order = decision.options.count() + 1
                opt = DecisionOption.objects.create(
                    decision=decision,
                    title=opt_title,
                    description=opt_desc,
                    order=next_order
                )
                record_timeline_event(decision, 'OPTION_ADDED', f"Added option: '{opt.title}'")
                messages.success(request, f"Option '{opt.title}' added.")

        # Action: Delete Option
        elif action == 'delete_option':
            opt_id = request.POST.get('option_id')
            opt = get_object_or_404(DecisionOption, id=opt_id, decision=decision)
            title = opt.title
            opt.delete()
            record_timeline_event(decision, 'OPTION_REMOVED', f"Removed option: '{title}'")
            messages.info(request, f"Option '{title}' removed.")

        # Action: Add Factor
        elif action == 'add_factor':
            fac_name = request.POST.get('factor_name', '').strip()
            fac_weight = int(request.POST.get('factor_weight', 5))
            fac_exp = request.POST.get('factor_explanation', '').strip()
            if fac_name:
                fac = DecisionFactor.objects.create(
                    decision=decision,
                    name=fac_name,
                    weight=max(1, min(10, fac_weight)),
                    explanation=fac_exp
                )
                record_timeline_event(decision, 'FACTOR_ADDED', f"Added criterion: '{fac.name}' (weight: {fac.weight})")
                messages.success(request, f"Factor '{fac.name}' added.")

        # Action: Delete Factor
        elif action == 'delete_factor':
            fac_id = request.POST.get('factor_id')
            fac = get_object_or_404(DecisionFactor, id=fac_id, decision=decision)
            name = fac.name
            fac.delete()
            record_timeline_event(decision, 'FACTOR_REMOVED', f"Removed criterion: '{name}'")
            messages.info(request, f"Factor '{name}' removed.")

        # Action: Save Factor Score Matrix
        elif action == 'update_scores':
            factors = decision.factors.all()
            options = decision.options.all()
            for fac in factors:
                for opt in options:
                    input_key = f"score_{fac.id}_{opt.id}"
                    if input_key in request.POST:
                        try:
                            val = int(request.POST.get(input_key, 5))
                            val = max(1, min(10, val))
                            FactorScore.objects.update_or_create(
                                factor=fac,
                                option=opt,
                                defaults={'score': val}
                            )
                        except (ValueError, TypeError):
                            pass
            record_timeline_event(decision, 'SCORES_UPDATED', "Evaluation scores updated")
            messages.success(request, "Evaluation ratings saved successfully.")

        # Action: Add Pro/Con
        elif action == 'add_pro_con':
            opt_id = request.POST.get('pc_option_id')
            pc_type = request.POST.get('pc_type')
            pc_text = request.POST.get('pc_text', '').strip()
            if opt_id and pc_type in ['PRO', 'CON'] and pc_text:
                opt = get_object_or_404(DecisionOption, id=opt_id, decision=decision)
                ProsCons.objects.create(option=opt, type=pc_type, text=pc_text)
                messages.success(request, f"Added {pc_type.lower()} to {opt.title}.")

        # Action: Delete Pro/Con
        elif action == 'delete_pro_con':
            pc_id = request.POST.get('pc_id')
            pc = get_object_or_404(ProsCons, id=pc_id, option__decision=decision)
            pc.delete()
            messages.info(request, "Item removed.")

        # Action: Final Decision Selection
        elif action == 'make_decision':
            selected_option_id = request.POST.get('selected_option')
            confidence = request.POST.get('confidence_score')
            reasoning = request.POST.get('decision_reasoning', '').strip()

            if selected_option_id and confidence:
                selected_opt = get_object_or_404(DecisionOption, id=selected_option_id, decision=decision)
                decision.selected_option = selected_opt
                decision.confidence_score = int(confidence)
                decision.decision_reasoning = reasoning
                decision.status = 'DECIDED'
                decision.decided_at = timezone.now()
                decision.save()

                record_timeline_event(
                    decision,
                    'DECISION_MADE',
                    f"Decision made: '{selected_opt.title}'",
                    f"Confidence: {decision.confidence_score}%. Rationale: {reasoning}"
                )
                messages.success(request, f"Decision recorded! Chosen option: {selected_opt.title}")
                return redirect('decision_detail', pk=decision.pk)
            else:
                messages.error(request, "Please select an option and indicate your confidence level.")

        return redirect('decision_wizard', pk=decision.pk)

    # Prepare data for rendering wizard
    analysis = calculate_decision_scores(decision)
    options = decision.options.all()
    factors = decision.factors.all()

    # Pre-build lookup of factor scores for matrix form
    scores_dict = {}
    for fs in FactorScore.objects.filter(factor__decision=decision):
        scores_dict[(fs.factor_id, fs.option_id)] = fs.score

    context = {
        'decision': decision,
        'options': options,
        'factors': factors,
        'analysis': analysis,
        'scores_dict': scores_dict,
    }
    return render(request, 'decisions/decision_wizard.html', context)


@login_required
def decision_detail_view(request, pk):
    """
    Comprehensive Decision Detail page:
    Shows structured overview, options with weighted scoring and rankings,
    criteria matrix, qualitative pros & cons, final verdict, timeline, and outcome.
    """
    decision = get_object_or_404(Decision, pk=pk, user=request.user)
    analysis = calculate_decision_scores(decision)
    events = decision.events.all()
    outcome = getattr(decision, 'outcome', None)

    context = {
        'decision': decision,
        'analysis': analysis,
        'events': events,
        'outcome': outcome,
    }
    return render(request, 'decisions/decision_detail.html', context)


@login_required
def decision_edit_view(request, pk):
    """
    Edits the high-level metadata (title, category, importance, deadline) of a decision.
    """
    decision = get_object_or_404(Decision, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DecisionBasicForm(request.POST, instance=decision)
        if form.is_valid():
            form.save()
            record_timeline_event(decision, 'UPDATED', "Decision metadata updated")
            messages.success(request, "Decision details updated.")
            return redirect('decision_detail', pk=decision.pk)
    else:
        form = DecisionBasicForm(instance=decision)

    return render(request, 'decisions/decision_form.html', {'form': form, 'title': 'Edit Decision Details', 'decision': decision})


@login_required
def decision_delete_view(request, pk):
    """
    Safely deletes a decision and all associated relational records.
    """
    decision = get_object_or_404(Decision, pk=pk, user=request.user)
    if request.method == 'POST':
        title = decision.title
        decision.delete()
        messages.success(request, f"Decision '{title}' has been deleted.")
        return redirect('decision_list')

    return render(request, 'decisions/decision_confirm_delete.html', {'decision': decision})


@login_required
def decision_outcome_view(request, pk):
    """
    Captures real-world retrospective results and satisfaction ratings.
    Transitions decision status to COMPLETED and unlocks Decision Replay.
    """
    decision = get_object_or_404(Decision, pk=pk, user=request.user)
    outcome = getattr(decision, 'outcome', None)

    if request.method == 'POST':
        form = OutcomeForm(request.POST, instance=outcome)
        if form.is_valid():
            new_outcome = form.save(commit=False)
            new_outcome.decision = decision
            new_outcome.save()

            # Advance status to completed
            decision.status = 'COMPLETED'
            decision.save()

            record_timeline_event(
                decision,
                'OUTCOME_RECORDED',
                f"Outcome recorded: {new_outcome.get_outcome_status_display()}",
                f"Satisfaction: {new_outcome.satisfaction_score}/10. Summary: {new_outcome.actual_result[:100]}"
            )
            messages.success(request, "Outcome recorded! Check out your Decision Replay comparison.")
            return redirect('decision_replay', pk=decision.pk)
    else:
        initial_data = {}
        if not outcome:
            initial_data = {
                'outcome_date': timezone.now().date(),
                'expected_result': decision.decision_reasoning or ''
            }
        form = OutcomeForm(instance=outcome, initial=initial_data)

    context = {
        'decision': decision,
        'form': form,
        'outcome': outcome,
    }
    return render(request, 'decisions/outcome_form.html', context)


@login_required
def decision_replay_view(request, pk):
    """
    Unique Decision Replay Feature:
    Side-by-side retrospective contrasting 'At Decision Time' vs 'After Outcome'.
    Evaluates original confidence vs reality and calculates prediction accuracy.
    """
    decision = get_object_or_404(Decision, pk=pk, user=request.user)
    replay_data = analyze_decision_replay(decision)

    context = {
        'decision': decision,
        'replay': replay_data,
        'outcome': getattr(decision, 'outcome', None),
        'events': decision.events.all(),
    }
    return render(request, 'decisions/decision_replay.html', context)


@login_required
def insights_view(request):
    """
    Historical Intelligence View:
    Computes holistic meta-patterns across the user's decision history.
    Finds most successful categories, confidence calibration, and alignment rates.
    """
    user = request.user
    decisions = Decision.objects.filter(user=user)
    outcomes = DecisionOutcome.objects.filter(decision__user=user).select_related('decision')

    total_decisions = decisions.count()
    completed_count = outcomes.count()

    # Category performance analysis
    category_stats = []
    for cat_code, cat_label in Decision.CATEGORY_CHOICES:
        cat_decisions = decisions.filter(category=cat_code)
        cat_total = cat_decisions.count()
        if cat_total > 0:
            cat_outcomes = outcomes.filter(decision__category=cat_code)
            cat_successful = cat_outcomes.filter(outcome_status='SUCCESSFUL').count()
            cat_completed = cat_outcomes.count()
            cat_success_rate = round((cat_successful / cat_completed * 100), 1) if cat_completed > 0 else 0
            
            avg_conf = cat_decisions.filter(confidence_score__isnull=False).aggregate(Avg('confidence_score'))['confidence_score__avg']
            category_stats.append({
                'code': cat_code,
                'label': cat_label,
                'total': cat_total,
                'completed': cat_completed,
                'successful': cat_successful,
                'success_rate': cat_success_rate,
                'avg_confidence': round(avg_conf, 1) if avg_conf else 0,
            })

    # Sort categories by success rate descending
    category_stats.sort(key=lambda x: (x['success_rate'], x['total']), reverse=True)
    best_category = category_stats[0] if category_stats and category_stats[0]['completed'] > 0 else None

    # Overall metrics
    avg_confidence = decisions.filter(confidence_score__isnull=False).aggregate(Avg('confidence_score'))['confidence_score__avg']
    avg_confidence = round(avg_confidence, 1) if avg_confidence else 0

    # Divergence analysis: decisions where user selected an option other than highest scoring
    divergent_decisions = []
    for dec in decisions.filter(selected_option__isnull=False).prefetch_related('options', 'factors'):
        calc = calculate_decision_scores(dec)
        if not calc.get('is_aligned') and calc.get('highest_scoring'):
            divergent_decisions.append({
                'decision': dec,
                'selected': dec.selected_option.title,
                'selected_score': calc['selected_result']['percentage'] if calc.get('selected_result') else 0,
                'top_option': calc['highest_scoring']['title'],
                'top_score': calc['highest_scoring']['percentage'],
                'difference': calc.get('score_difference', 0),
            })

    context = {
        'total_decisions': total_decisions,
        'completed_count': completed_count,
        'category_stats': category_stats,
        'best_category': best_category,
        'avg_confidence': avg_confidence,
        'divergent_decisions': divergent_decisions,
    }
    return render(request, 'decisions/insights.html', context)
