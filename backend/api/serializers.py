from rest_framework import serializers
from .models import User, Site, Agent, MikrotikDevice

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
        read_only_fields = ['user']

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class MikrotikDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MikrotikDevice
        fields = '__all__'
