"""
TimeVault Test Suite
Comprehensive testing coverage across Models, Scoring Engine,
Authentication, User Isolation, View Workflows, and Edge Cases.
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from .models import (
    Decision, DecisionOption, DecisionFactor, FactorScore,
    ProsCons, DecisionOutcome, DecisionEvent
)
from .services import (
    calculate_decision_scores, analyze_decision_replay, record_timeline_event
)


class ScoringEngineTests(TestCase):
    """
    Validates mathematical accuracy of the Multi-Criteria Decision Analysis engine.
    """
    def setUp(self):
        self.user = User.objects.create_user(username="math_user", password="password123")
        self.decision = Decision.objects.create(
            user=self.user,
            title="Test Decision Math",
            category="CAREER"
        )

    def test_weighted_scoring_known_values(self):
        # Create 2 options
        opt_a = DecisionOption.objects.create(decision=self.decision, title="Option Alpha", order=1)
        opt_b = DecisionOption.objects.create(decision=self.decision, title="Option Beta", order=2)

        # Factor 1: Weight 10
        fac_1 = DecisionFactor.objects.create(decision=self.decision, name="Salary", weight=10)
        # Factor 2: Weight 5
        fac_2 = DecisionFactor.objects.create(decision=self.decision, name="Commute", weight=5)

        # Total Weight = 15. Max possible score = 15 * 10 = 150.
        # Option Alpha: fac_1 score=8 (wt:10 -> 80), fac_2 score=6 (wt:5 -> 30) -> Sum = 110. Pct = (110/150)*100 = 73.3%
        # Option Beta:  fac_1 score=6 (wt:10 -> 60), fac_2 score=10 (wt:5 -> 50) -> Sum = 110. Pct = 73.3%
        FactorScore.objects.create(factor=fac_1, option=opt_a, score=8)
        FactorScore.objects.create(factor=fac_2, option=opt_a, score=6)

        FactorScore.objects.create(factor=fac_1, option=opt_b, score=6)
        FactorScore.objects.create(factor=fac_2, option=opt_b, score=10)

        results = calculate_decision_scores(self.decision)
        self.assertEqual(results['total_factors'], 2)
        self.assertEqual(results['total_weight'], 15)
        self.assertEqual(results['max_possible_score'], 150)

        opt_a_res = next(o for o in results['options'] if o['id'] == opt_a.id)
        self.assertEqual(opt_a_res['weighted_sum'], 110)
        self.assertEqual(opt_a_res['percentage'], 73.3)

    def test_edge_case_no_factors(self):
        DecisionOption.objects.create(decision=self.decision, title="Solo Option")
        results = calculate_decision_scores(self.decision)
        self.assertEqual(results['total_factors'], 0)
        self.assertEqual(results['total_weight'], 0)
        self.assertEqual(results['options'][0]['percentage'], 0.0)

    def test_edge_case_no_options(self):
        DecisionFactor.objects.create(decision=self.decision, name="Salary", weight=5)
        results = calculate_decision_scores(self.decision)
        self.assertEqual(len(results['options']), 0)
        self.assertIsNone(results['highest_scoring'])


class UserDataIsolationTests(TestCase):
    """
    Enforces strict security boundary: User A cannot see or mutate User B's decisions.
    """
    def setUp(self):
        self.user_a = User.objects.create_user(username="alice", password="alicepassword")
        self.user_b = User.objects.create_user(username="bob", password="bobpassword")

        self.dec_a = Decision.objects.create(
            user=self.user_a,
            title="Alice Private Career Decision"
        )
        self.client_b = Client()
        self.client_b.login(username="bob", password="bobpassword")

    def test_user_b_cannot_view_user_a_decision(self):
        response = self.client_b.get(reverse('decision_detail', kwargs={'pk': self.dec_a.pk}))
        self.assertEqual(response.status_code, 404)

    def test_user_b_cannot_access_user_a_wizard(self):
        response = self.client_b.get(reverse('decision_wizard', kwargs={'pk': self.dec_a.pk}))
        self.assertEqual(response.status_code, 404)

    def test_user_b_cannot_delete_user_a_decision(self):
        response = self.client_b.post(reverse('decision_delete', kwargs={'pk': self.dec_a.pk}))
        self.assertEqual(response.status_code, 404)
        # Verify dec_a still exists in database
        self.assertTrue(Decision.objects.filter(pk=self.dec_a.pk).exists())


class AuthenticationAndViewsWorkflowTests(TestCase):
    """
    Tests end-to-end user workflows from signup, decision creation, wizard, to outcome.
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testrunner", password="securepassword123")

    def test_registration_flow(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'StrongP@ss1234',
            'password2': 'StrongP@ss1234',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_unauthenticated_redirect(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_decision_lifecycle_workflow(self):
        self.client.login(username="testrunner", password="securepassword123")

        # 1. Dashboard loads
        dash_res = self.client.get(reverse('dashboard'))
        self.assertEqual(dash_res.status_code, 200)

        # 2. Create Decision
        create_res = self.client.post(reverse('decision_create'), {
            'title': 'Relocate to Tokyo',
            'description': 'Evaluating opportunity in Japan',
            'category': 'PERSONAL',
            'importance': 'HIGH',
            'deadline': (timezone.now() + timedelta(days=30)).date(),
        })
        self.assertEqual(create_res.status_code, 302)
        dec = Decision.objects.get(title='Relocate to Tokyo')
        self.assertEqual(dec.user, self.user)

        # 3. Add Option via Wizard
        self.client.post(reverse('decision_wizard', kwargs={'pk': dec.pk}), {
            'action': 'add_option',
            'option_title': 'Option 1: Move to Tokyo',
            'option_description': 'Full relocation'
        })
        self.assertEqual(dec.options.count(), 1)
        opt = dec.options.first()

        # 4. Add Factor via Wizard
        self.client.post(reverse('decision_wizard', kwargs={'pk': dec.pk}), {
            'action': 'add_factor',
            'factor_name': 'Adventure & Culture',
            'factor_weight': '9',
            'factor_explanation': 'Personal enrichment'
        })
        self.assertEqual(dec.factors.count(), 1)
        fac = dec.factors.first()

        # 5. Score Matrix
        self.client.post(reverse('decision_wizard', kwargs={'pk': dec.pk}), {
            'action': 'update_scores',
            f'score_{fac.id}_{opt.id}': '9'
        })
        fs = FactorScore.objects.get(factor=fac, option=opt)
        self.assertEqual(fs.score, 9)

        # 6. Finalize Decision
        decide_res = self.client.post(reverse('decision_wizard', kwargs={'pk': dec.pk}), {
            'action': 'make_decision',
            'selected_option': opt.id,
            'confidence_score': '88',
            'decision_reasoning': 'Compelling cultural experience and adventure.'
        })
        self.assertEqual(decide_res.status_code, 302)
        dec.refresh_from_db()
        self.assertEqual(dec.status, 'DECIDED')
        self.assertEqual(dec.selected_option, opt)
        self.assertEqual(dec.confidence_score, 88)

        # 7. Record Outcome
        outcome_res = self.client.post(reverse('decision_outcome', kwargs={'pk': dec.pk}), {
            'outcome_status': 'SUCCESSFUL',
            'actual_result': 'Relocation was extraordinary and smooth.',
            'satisfaction_score': '9',
            'outcome_date': timezone.now().date(),
            'financial_impact': 'Neutral',
            'what_went_right': 'Great community',
            'what_went_wrong': 'Initial paperwork',
            'lessons_learned': 'Embrace unfamiliar challenges'
        })
        self.assertEqual(outcome_res.status_code, 302)
        dec.refresh_from_db()
        self.assertEqual(dec.status, 'COMPLETED')
        self.assertTrue(hasattr(dec, 'outcome'))

        # 8. Decision Replay view loads
        replay_res = self.client.get(reverse('decision_replay', kwargs={'pk': dec.pk}))
        self.assertEqual(replay_res.status_code, 200)
        self.assertContains(replay_res, 'Longitudinal Judgment Calibration')

        # 9. Insights page loads
        insights_res = self.client.get(reverse('insights'))
        self.assertEqual(insights_res.status_code, 200)
        self.assertContains(insights_res, 'Personal')
