from django.urls import path
from .views import  AgentRegistrationView, AgentSyncView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('agents/register/', AgentRegistrationView.as_view(), name='agent_register'),
    path('agents/<uuid:agent_id>/sync/', AgentSyncView.as_view(), name='agent_sync'),
]
