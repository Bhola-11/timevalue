"""
TimeVault Form Definitions
Provides validated inputs for authentication, decision initialization, options,
factors, final choice selection, and longitudinal outcome logging.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Decision, DecisionOption, DecisionFactor, DecisionOutcome, ProsCons


class UserRegistrationForm(UserCreationForm):
    """
    User registration form with email and full name requirements.
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'name@example.com'}))
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Choose username'})
        for fieldname in ['password1', 'password2']:
            if fieldname in self.fields:
                self.fields[fieldname].widget.attrs.update({'class': 'form-input', 'placeholder': '••••••••'})


class DecisionBasicForm(forms.ModelForm):
    """
    Step 1: Basic Decision Information Form.
    """
    class Meta:
        model = Decision
        fields = ['title', 'description', 'category', 'importance', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Should I accept the offer from Tech Corp?'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Provide context, background, and what is at stake...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'importance': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }


class FinalDecisionForm(forms.ModelForm):
    """
    Step 6 / Final Decision Form: Choose selected option, confidence, and reasoning.
    """
    class Meta:
        model = Decision
        fields = ['selected_option', 'confidence_score', 'decision_reasoning']
        widgets = {
            'selected_option': forms.Select(attrs={'class': 'form-select'}),
            'confidence_score': forms.NumberInput(attrs={'class': 'form-input', 'min': '1', 'max': '100', 'placeholder': '1-100%'}),
            'decision_reasoning': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Explain your rational conviction and why you chose this path...'}),
        }

    def __init__(self, *args, **kwargs):
        decision = kwargs.pop('decision', None)
        super().__init__(*args, **kwargs)
        if decision:
            self.fields['selected_option'].queryset = decision.options.all()
            self.fields['selected_option'].required = True
            self.fields['confidence_score'].required = True
            self.fields['decision_reasoning'].required = True


class OutcomeForm(forms.ModelForm):
    """
    Outcome Evaluation Form: Captures real-world consequences and reflections.
    """
    class Meta:
        model = DecisionOutcome
        fields = [
            'outcome_status', 'actual_result', 'expected_result', 'satisfaction_score',
            'outcome_date', 'financial_impact', 'what_went_right', 'what_went_wrong', 'lessons_learned'
        ]
        widgets = {
            'outcome_status': forms.Select(attrs={'class': 'form-select'}),
            'actual_result': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'What actually unfolded in reality?'}),
            'expected_result': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 2, 'placeholder': 'What did you anticipate back then?'}),
            'satisfaction_score': forms.NumberInput(attrs={'class': 'form-input', 'min': '1', 'max': '10', 'placeholder': '1 (Regret) to 10 (Thriving)'}),
            'outcome_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'financial_impact': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. +$20,000 compensation increase / No direct cost'}),
            'what_went_right': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Key positive realizations and wins...'}),
            'what_went_wrong': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Unforeseen friction, setbacks or missed assumptions...'}),
            'lessons_learned': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Actionable wisdom for future decisions...'}),
        }
