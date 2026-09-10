"""
TimeVault Test Suite
Unit and integration tests for Decision Intelligence models, MCDA engine, and workflows.
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from decisions.models import (
    Decision, DecisionOption, DecisionFactor, FactorScore,
    ProsCons, DecisionOutcome, DecisionEvent
)
from decisions.services import calculate_decision_scores, analyze_decision_replay

class CoreDecisionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testrunner", password="password123")
        self.decision = Decision.objects.create(
            user=self.user,
            title="Relocation Decision Matrix",
            category="CAREER"
        )

    def test_mcda_scoring_calculation(self):
        opt_a = DecisionOption.objects.create(decision=self.decision, title="Relocate to Seattle")
        opt_b = DecisionOption.objects.create(decision=self.decision, title="Stay Remote")
        fac_comp = DecisionFactor.objects.create(decision=self.decision, name="Compensation", weight=10)
        fac_wlb = DecisionFactor.objects.create(decision=self.decision, name="Work-Life Balance", weight=8)

        FactorScore.objects.create(factor=fac_comp, option=opt_a, score=9)
        FactorScore.objects.create(factor=fac_comp, option=opt_b, score=6)
        FactorScore.objects.create(factor=fac_wlb, option=opt_a, score=6)
        FactorScore.objects.create(factor=fac_wlb, option=opt_b, score=9)

        res = calculate_decision_scores(self.decision)
        self.assertEqual(res['total_factors'], 2)
        self.assertEqual(res['total_weight'], 18)
        self.assertGreater(len(res['options']), 0)

    def test_user_data_isolation(self):
        other_user = User.objects.create_user(username="otheruser", password="password123")
        client = Client()
        client.login(username="otheruser", password="password123")
        response = client.get(reverse('decision_detail', kwargs={'pk': self.decision.pk}))
        self.assertEqual(response.status_code, 404)
