from rest_framework import serializers

from .models import ServiceInfo


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = "__all__"
