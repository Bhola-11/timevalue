"""
TimeVault Demo Data Seeder
Populates a standalone demo user with representative multi-domain decisions,
scoring matrices, timeline events, and longitudinal outcomes.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from decisions.models import (
    Decision, DecisionOption, DecisionFactor, FactorScore,
    ProsCons, DecisionOutcome, DecisionEvent
)


class Command(BaseCommand):
    help = "Seeds high-fidelity demo decision data for testing and demonstration."

    def handle(self, *args, **options):
        self.stdout.write("Initializing TimeVault demo data...")

        demo_user, created = User.objects.get_or_create(
            username="demo_user",
            defaults={
                "email": "demo@timevault.local",
                "first_name": "Demo",
                "last_name": "Architect",
            }
        )
        if created:
            demo_user.set_password("demopass123")
            demo_user.save()
            self.stdout.write(self.style.SUCCESS("Created demo user: 'demo_user' (password: demopass123)"))
        else:
            self.stdout.write("Found existing demo user 'demo_user'. Updating demo records...")

        # -------------------------------------------------------------
        # Decision 1: Career Offer (Completed with Outcome)
        # -------------------------------------------------------------
        dec1, _ = Decision.objects.update_or_create(
            user=demo_user,
            title="Should I accept the Principal Architect offer at NovaTech?",
            defaults={
                "description": "NovaTech offered a Principal Systems Architect role with a 35% base raise and equity, but requires relocating to Seattle and shifting from hands-on coding to architecture oversight.",
                "category": "CAREER",
                "importance": "CRITICAL",
                "status": "COMPLETED",
                "deadline": (timezone.now() - timedelta(days=120)).date(),
                "decided_at": timezone.now() - timedelta(days=115),
                "confidence_score": 85,
                "decision_reasoning": "The long-term career growth, compensation step-up, and scale of distributed systems outweigh the relocation friction.",
            }
        )

        opt1_a, _ = DecisionOption.objects.get_or_create(
            decision=dec1, title="Accept NovaTech Offer",
            defaults={"description": "Relocate to Seattle, $210k base + equity, leadership focus.", "order": 1}
        )
        opt1_b, _ = DecisionOption.objects.get_or_create(
            decision=dec1, title="Stay at Current Company",
            defaults={"description": "Stay Senior Eng, remote, high autonomy, $155k base.", "order": 2}
        )
        opt1_c, _ = DecisionOption.objects.get_or_create(
            decision=dec1, title="Counter-Offer Current Company",
            defaults={"description": "Ask current company for promotion to Staff Eng with raise to $175k.", "order": 3}
        )

        dec1.selected_option = opt1_a
        dec1.save()

        # Factors
        fac_comp, _ = DecisionFactor.objects.get_or_create(
            decision=dec1, name="Total Compensation & Equity",
            defaults={"weight": 9, "explanation": "Direct financial trajectory and wealth building."}
        )
        fac_growth, _ = DecisionFactor.objects.get_or_create(
            decision=dec1, name="Long-Term Career Growth",
            defaults={"weight": 10, "explanation": "Stepping stone to VP of Engineering / CTO."}
        )
        fac_wlb, _ = DecisionFactor.objects.get_or_create(
            decision=dec1, name="Work-Life Balance & Remote Flexibility",
            defaults={"weight": 7, "explanation": "Avoid burnout and maintain personal time."}
        )
        fac_culture, _ = DecisionFactor.objects.get_or_create(
            decision=dec1, name="Team Culture & Engineering Rigor",
            defaults={"weight": 8, "explanation": "Working with world-class peers."}
        )

        # Factor Scores Matrix
        matrix_scores_1 = [
            (fac_comp, opt1_a, 9), (fac_comp, opt1_b, 5), (fac_comp, opt1_c, 7),
            (fac_growth, opt1_a, 10), (fac_growth, opt1_b, 4), (fac_growth, opt1_c, 6),
            (fac_wlb, opt1_a, 6), (fac_wlb, opt1_b, 9), (fac_wlb, opt1_c, 7),
            (fac_culture, opt1_a, 9), (fac_culture, opt1_b, 7), (fac_culture, opt1_c, 7),
        ]
        for f, o, sc in matrix_scores_1:
            FactorScore.objects.update_or_create(factor=f, option=o, defaults={"score": sc})

        # Pros and Cons
        ProsCons.objects.get_or_create(option=opt1_a, type="PRO", text="Substantial $55k base raise and high upside RSUs")
        ProsCons.objects.get_or_create(option=opt1_a, type="PRO", text="Expands network in top-tier Pacific Northwest tech hub")
        ProsCons.objects.get_or_create(option=opt1_a, type="CON", text="Relocation logistics and leaving established routine")
        ProsCons.objects.get_or_create(option=opt1_b, type="PRO", text="Comfortable, low stress, established trust")
        ProsCons.objects.get_or_create(option=opt1_b, type="CON", text="Stagnating technical challenges and compensation ceiling")

        # Outcome
        DecisionOutcome.objects.update_or_create(
            decision=dec1,
            defaults={
                "outcome_status": "SUCCESSFUL",
                "satisfaction_score": 9,
                "outcome_date": (timezone.now() - timedelta(days=15)).date(),
                "financial_impact": "+$62,000 net compensation step-up in Year 1",
                "actual_result": "Relocated smoothly. Promoted to lead two engineering squads within 6 months. Culture is demanding but exceptionally supportive.",
                "expected_result": "Anticipated initial cultural ramp-up stress but sustained long-term leadership trajectory.",
                "what_went_right": "The technical challenges matched expectations and the team embraced architectural modernization.",
                "what_went_wrong": "Underestimated housing costs in Seattle initially during the first 2 months.",
                "lessons_learned": "High-confidence career pivots payoff when the growth criterion is explicitly weighted at 10.",
            }
        )

        # Timeline events
        DecisionEvent.objects.get_or_create(
            decision=dec1, event_type="CREATED", title="Decision initialized",
            defaults={"description": "Started formal evaluation between NovaTech and current role."}
        )
        DecisionEvent.objects.get_or_create(
            decision=dec1, event_type="DECISION_MADE", title="Decision finalized: Accept NovaTech",
            defaults={"description": "Confidence rated at 85%. Rationale documented."}
        )
        DecisionEvent.objects.get_or_create(
            decision=dec1, event_type="OUTCOME_RECORDED", title="Retrospective outcome evaluated",
            defaults={"description": "Rated Successful (9/10 satisfaction)."}
        )

        # -------------------------------------------------------------
        # Decision 2: Relocation / Lifestyle (Completed with Outcome)
        # -------------------------------------------------------------
        dec2, _ = Decision.objects.update_or_create(
            user=demo_user,
            title="Relocate to Zurich for International Exposure",
            defaults={
                "description": "Considered moving abroad to Zurich, Switzerland for 2 years to experience living in Central Europe.",
                "category": "PERSONAL",
                "importance": "HIGH",
                "status": "COMPLETED",
                "deadline": (timezone.now() - timedelta(days=200)).date(),
                "decided_at": timezone.now() - timedelta(days=190),
                "confidence_score": 65,
                "decision_reasoning": "Valued adventure and alpine lifestyle over short-term tax/administrative friction.",
            }
        )
        opt2_a, _ = DecisionOption.objects.get_or_create(
            decision=dec2, title="Move to Zurich", defaults={"order": 1}
        )
        opt2_b, _ = DecisionOption.objects.get_or_create(
            decision=dec2, title="Stay Local & Travel More", defaults={"order": 2}
        )
        dec2.selected_option = opt2_a
        dec2.save()

        fac2_exp, _ = DecisionFactor.objects.get_or_create(
            decision=dec2, name="Cultural & Life Adventure", defaults={"weight": 9}
        )
        fac2_cost, _ = DecisionFactor.objects.get_or_create(
            decision=dec2, name="Cost of Living & Setup Friction", defaults={"weight": 7}
        )
        FactorScore.objects.update_or_create(factor=fac2_exp, option=opt2_a, defaults={"score": 9})
        FactorScore.objects.update_or_create(factor=fac2_exp, option=opt2_b, defaults={"score": 5})
        FactorScore.objects.update_or_create(factor=fac2_cost, option=opt2_a, defaults={"score": 4})
        FactorScore.objects.update_or_create(factor=fac2_cost, option=opt2_b, defaults={"score": 8})

        DecisionOutcome.objects.update_or_create(
            decision=dec2,
            defaults={
                "outcome_status": "NEUTRAL",
                "satisfaction_score": 6,
                "outcome_date": (timezone.now() - timedelta(days=30)).date(),
                "financial_impact": "-$8,000 initial international transition overhead",
                "actual_result": "Incredible outdoors and train travel, but bureaucratic friction and social isolation in winter were harder than forecasted.",
                "what_went_right": "Explored Swiss Alps extensively and mastered conversational German.",
                "what_went_wrong": "Apartment hunting took 3 months and integration was slow.",
                "lessons_learned": "Social integration speed must be an explicit weighted factor in relocation models.",
            }
        )

        # -------------------------------------------------------------
        # Decision 3: Business Model (Decided, Pending Outcome)
        # -------------------------------------------------------------
        dec3, _ = Decision.objects.update_or_create(
            user=demo_user,
            title="Bootstrap SaaS Product vs Pitch Seed VCs",
            defaults={
                "description": "Launching an developer telemetry SaaS. Decide between self-funding to profitability vs raising an institutional pre-seed round.",
                "category": "BUSINESS",
                "importance": "CRITICAL",
                "status": "DECIDED",
                "deadline": (timezone.now() + timedelta(days=10)).date(),
                "decided_at": timezone.now() - timedelta(days=5),
                "confidence_score": 78,
                "decision_reasoning": "Retaining 100% equity and full customer-driven roadmap control aligns better with our sustainable profitability vision.",
            }
        )
        opt3_a, _ = DecisionOption.objects.get_or_create(
            decision=dec3, title="Bootstrap to Profitability", defaults={"order": 1}
        )
        opt3_b, _ = DecisionOption.objects.get_or_create(
            decision=dec3, title="Raise $1M Pre-Seed from Angels/VC", defaults={"order": 2}
        )
        dec3.selected_option = opt3_a
        dec3.save()

        fac3_ctl, _ = DecisionFactor.objects.get_or_create(
            decision=dec3, name="Ownership & Autonomy", defaults={"weight": 10}
        )
        fac3_spd, _ = DecisionFactor.objects.get_or_create(
            decision=dec3, name="Speed to Market", defaults={"weight": 8}
        )
        FactorScore.objects.update_or_create(factor=fac3_ctl, option=opt3_a, defaults={"score": 10})
        FactorScore.objects.update_or_create(factor=fac3_ctl, option=opt3_b, defaults={"score": 4})
        FactorScore.objects.update_or_create(factor=fac3_spd, option=opt3_a, defaults={"score": 6})
        FactorScore.objects.update_or_create(factor=fac3_spd, option=opt3_b, defaults={"score": 9})

        self.stdout.write(self.style.SUCCESS("TimeVault demo data seeded successfully!"))
        self.stdout.write("Credentials: Username 'demo_user' | Password 'demopass123'")
