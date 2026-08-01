from rest_framework import viewsets, status,  generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Site, Agent, MikrotikDevice, User
from .serializers import UserSerializer, SiteSerializer, AgentSerializer, MikrotikDeviceSerializer
from django.utils import timezone

# --- CONFIGURATION LOGIQUE D'AUTH ---
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Site.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AgentViewSet(viewsets.ModelViewSet):
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Agent.objects.filter(site__user=self.request.user)

class MikrotikDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = MikrotikDeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MikrotikDevice.objects.filter(agent__site__user=self.request.user)

class AgentRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        agent_code = request.data.get('agent_code')
        site_id = request.data.get('site_id')
        
        if not agent_code or not site_id:
            return Response({'error': 'agent_code and site_id are required'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            site = Site.objects.get(id=site_id, user=request.user)
            agent = Agent.objects.get(agent_code=agent_code)
            agent.site = site
            agent.save()
            return Response(AgentSerializer(agent).data)
        except Site.DoesNotExist:
            return Response({'error': 'Site not found'}, status=status.HTTP_404_NOT_FOUND)
        except Agent.DoesNotExist:
            # Here we might auto-create the agent if we want, but for security, the agent should connect first to generate its code.
            return Response({'error': 'Agent code not recognized'}, status=status.HTTP_404_NOT_FOUND)

class AgentSyncView(APIView):
    permission_classes = [AllowAny] # In real app, we use a specific API key or the Agent ID itself for auth

    def post(self, request, agent_id):
        try:
            agent = Agent.objects.get(id=agent_id)
        except Agent.DoesNotExist:
            # If agent doesn't exist, we create it. This is how agents "register" their existence before being assigned a site
            agent_code = request.data.get('agent_code')
            if not agent_code:
                return Response({'error': 'agent_code required for new agents'}, status=status.HTTP_400_BAD_REQUEST)
            agent = Agent.objects.create(id=agent_id, agent_code=agent_code, status='online', last_seen=timezone.now())

        agent.status = 'online'
        agent.last_seen = timezone.now()
        agent.local_ip = request.data.get('local_ip', agent.local_ip)
        agent.save()

        devices_data = request.data.get('devices', [])
        current_device_ids = []
        for dev_data in devices_data:
            device, created = MikrotikDevice.objects.update_or_create(
                agent=agent,
                mac_address=dev_data.get('mac_address'),
                defaults={
                    'identity': dev_data.get('identity'),
                    'ip_address': dev_data.get('ip_address'),
                    'model': dev_data.get('model'),
                    'routeros_version': dev_data.get('routeros_version'),
                    'status': 'online',
                    'last_seen': timezone.now()
                }
            )
            current_device_ids.append(device.id)

        # Mark devices not seen as offline
        MikrotikDevice.objects.filter(agent=agent).exclude(id__in=current_device_ids).update(status='offline')

        return Response({'status': 'ok'})

