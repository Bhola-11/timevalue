"""
TimeVault Django Admin Configuration
Provides staff inspection and audit tools for decisions, options, criteria,
scoring entries, outcomes, and timeline logs.
"""
from django.contrib import admin
from .models import (
    Decision, DecisionOption, DecisionFactor, FactorScore,
    ProsCons, DecisionOutcome, DecisionEvent
)


class DecisionOptionInline(admin.TabularInline):
    model = DecisionOption
    extra = 0


class DecisionFactorInline(admin.TabularInline):
    model = DecisionFactor
    extra = 0


class DecisionEventInline(admin.TabularInline):
    model = DecisionEvent
    extra = 0
    readonly_fields = ('event_type', 'title', 'description', 'created_at')


@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'importance', 'status', 'deadline', 'confidence_score', 'updated_at')
    list_filter = ('status', 'category', 'importance', 'created_at')
    search_fields = ('title', 'description', 'user__username', 'user__email')
    ordering = ('-updated_at',)
    inlines = [DecisionOptionInline, DecisionFactorInline, DecisionEventInline]


@admin.register(DecisionOption)
class DecisionOptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'decision', 'order', 'created_at')
    list_filter = ('decision__category',)
    search_fields = ('title', 'description', 'decision__title')


@admin.register(DecisionFactor)
class DecisionFactorAdmin(admin.ModelAdmin):
    list_display = ('name', 'decision', 'weight', 'created_at')
    list_filter = ('weight',)
    search_fields = ('name', 'explanation', 'decision__title')


@admin.register(FactorScore)
class FactorScoreAdmin(admin.ModelAdmin):
    list_display = ('factor', 'option', 'score', 'notes')
    list_filter = ('score',)
    search_fields = ('factor__name', 'option__title')


@admin.register(ProsCons)
class ProsConsAdmin(admin.ModelAdmin):
    list_display = ('text', 'option', 'type', 'created_at')
    list_filter = ('type',)
    search_fields = ('text', 'option__title')


@admin.register(DecisionOutcome)
class DecisionOutcomeAdmin(admin.ModelAdmin):
    list_display = ('decision', 'outcome_status', 'satisfaction_score', 'outcome_date', 'updated_at')
    list_filter = ('outcome_status', 'satisfaction_score', 'outcome_date')
    search_fields = ('decision__title', 'actual_result', 'lessons_learned')


@admin.register(DecisionEvent)
class DecisionEventAdmin(admin.ModelAdmin):
    list_display = ('decision', 'event_type', 'title', 'created_at')
    list_filter = ('event_type', 'created_at')
    search_fields = ('title', 'description', 'decision__title')
