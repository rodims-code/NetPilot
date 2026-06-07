import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=50, blank=True, null=True)

class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sites')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='agents', null=True, blank=True)
    agent_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    local_ip = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, default='offline')
    last_seen = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agent_code} - {self.name}"

class MikrotikDevice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='devices')
    identity = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    board_name = models.CharField(max_length=255, blank=True, null=True)
    routeros_version = models.CharField(max_length=50, blank=True, null=True)
    architecture = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    mac_address = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, default='offline')
    last_seen = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.identity or self.ip_address or str(self.id)

