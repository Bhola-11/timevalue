"""
TimeVault Data Models
Defines the relational architecture for decisions, options, factors, scores,
outcomes, and timeline events with strict data validation and integrity.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Decision(models.Model):
    """
    Represents a primary life or business decision.
    Tracks state, importance, deadline, confidence, and chosen outcome.
    """
    CATEGORY_CHOICES = [
        ('CAREER', 'Career'),
        ('EDUCATION', 'Education'),
        ('FINANCE', 'Finance'),
        ('PERSONAL', 'Personal'),
        ('BUSINESS', 'Business'),
        ('TECHNOLOGY', 'Technology'),
        ('TRAVEL', 'Travel'),
        ('PURCHASE', 'Purchase'),
        ('RELATIONSHIPS', 'Relationships'),
        ('OTHER', 'Other'),
    ]

    IMPORTANCE_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('DECIDED', 'Decided'),
        ('OUTCOME_PENDING', 'Outcome Pending'),
        ('COMPLETED', 'Completed'),
        ('ARCHIVED', 'Archived'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decisions')
    title = models.CharField(max_length=255, help_text="e.g. 'Should I accept the Senior Engineer offer at Company X?'")
    description = models.TextField(blank=True, help_text="Detailed context, motivations, and background.")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='CAREER')
    importance = models.CharField(max_length=15, choices=IMPORTANCE_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    deadline = models.DateField(null=True, blank=True, help_text="Target date to make the decision")
    
    # Final decision fields
    decided_at = models.DateTimeField(null=True, blank=True)
    selected_option = models.ForeignKey(
        'DecisionOption',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='chosen_in_decisions'
    )
    confidence_score = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Confidence level from 1% to 100%"
    )
    decision_reasoning = models.TextField(blank=True, help_text="Why this option was chosen over alternatives")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['user', 'category']),
        ]

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


class DecisionOption(models.Model):
    """
    Represents an alternative path or candidate choice within a decision.
    """
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, related_name='options')
    title = models.CharField(max_length=200, help_text="e.g. 'Accept Offer A (Hybrid, San Francisco)'")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} [Decision #{self.decision_id}]"


class DecisionFactor(models.Model):
    """
    Represents an evaluation criterion (e.g. Salary, Work-Life Balance, Growth).
    Weight is rated 1 (least important) to 10 (most critical).
    """
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, related_name='factors')
    name = models.CharField(max_length=200, help_text="Criterion name")
    weight = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Importance weight (1-10)"
    )
    explanation = models.TextField(blank=True, help_text="Context on why this factor matters")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-weight', 'id']

    def __str__(self):
        return f"{self.name} (wt: {self.weight})"


class FactorScore(models.Model):
    """
    Stores the quantitative rating (1-10) of a specific Option for a specific Factor.
    """
    factor = models.ForeignKey(DecisionFactor, on_delete=models.CASCADE, related_name='scores')
    option = models.ForeignKey(DecisionOption, on_delete=models.CASCADE, related_name='factor_scores')
    score = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rating (1-10)"
    )
    notes = models.CharField(max_length=255, blank=True, help_text="Brief rationale for this rating")

    class Meta:
        unique_together = ('factor', 'option')

    def __str__(self):
        return f"{self.factor.name} -> {self.option.title}: {self.score}/10"


class ProsCons(models.Model):
    """
    Qualitative pros and cons associated with a specific option.
    """
    TYPE_CHOICES = [
        ('PRO', 'Pro'),
        ('CON', 'Con'),
    ]

    option = models.ForeignKey(DecisionOption, on_delete=models.CASCADE, related_name='pros_cons')
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['type', 'id']

    def __str__(self):
        return f"[{self.get_type_display()}] {self.text[:30]}"


class DecisionOutcome(models.Model):
    """
    Longitudinal outcome evaluation recorded after the decision has played out.
    Allows comparing predictions against reality.
    """
    OUTCOME_STATUS_CHOICES = [
        ('SUCCESSFUL', 'Successful'),
        ('NEUTRAL', 'Neutral'),
        ('UNSUCCESSFUL', 'Unsuccessful'),
    ]

    decision = models.OneToOneField(Decision, on_delete=models.CASCADE, related_name='outcome')
    outcome_status = models.CharField(max_length=15, choices=OUTCOME_STATUS_CHOICES)
    actual_result = models.TextField(help_text="What actually happened in reality")
    expected_result = models.TextField(blank=True, help_text="What was anticipated at decision time")
    satisfaction_score = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Retrospective satisfaction rating (1-10)"
    )
    outcome_date = models.DateField(help_text="Date when outcome was evaluated")
    financial_impact = models.CharField(max_length=200, blank=True, help_text="Measurable financial or career outcome")
    what_went_right = models.TextField(blank=True)
    what_went_wrong = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Outcome for {self.decision.title}: {self.get_outcome_status_display()}"


class DecisionEvent(models.Model):
    """
    Audit and progression timeline log for notable lifecycle events.
    """
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"[{self.created_at.strftime('%Y-%m-%d %H:%M')}] {self.title}"
