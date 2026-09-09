"""
TimeVault URL Configuration
Maps route endpoints to respective view controllers.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Dashboard & Root
    path('', views.dashboard_view, name='dashboard'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Decisions Lifecycle
    path('decisions/', views.decision_list_view, name='decision_list'),
    path('decisions/create/', views.decision_create_view, name='decision_create'),
    path('decisions/<int:pk>/', views.decision_detail_view, name='decision_detail'),
    path('decisions/<int:pk>/edit/', views.decision_edit_view, name='decision_edit'),
    path('decisions/<int:pk>/delete/', views.decision_delete_view, name='decision_delete'),
    path('decisions/<int:pk>/wizard/', views.decision_wizard_view, name='decision_wizard'),
    
    # Longitudinal Evaluation & Retrospective
    path('decisions/<int:pk>/outcome/', views.decision_outcome_view, name='decision_outcome'),
    path('decisions/<int:pk>/replay/', views.decision_replay_view, name='decision_replay'),
    
    # Historical Intelligence
    path('insights/', views.insights_view, name='insights'),
]
