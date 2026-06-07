from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet, AgentViewSet, MikrotikDeviceViewSet, AgentRegistrationView, AgentSyncView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'sites', SiteViewSet, basename='site')
router.register(r'agents', AgentViewSet, basename='agent')
router.register(r'devices', MikrotikDeviceViewSet, basename='device')

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('agents/register/', AgentRegistrationView.as_view(), name='agent_register'),
    path('agents/<uuid:agent_id>/sync/', AgentSyncView.as_view(), name='agent_sync'),
    path('', include(router.urls)),
]
