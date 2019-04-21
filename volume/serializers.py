from rest_framework import serializers

from .models import VolumeInfo


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeInfo
        fields = '__all__'
