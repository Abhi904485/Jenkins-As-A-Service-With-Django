from rest_framework import serializers

from .models import TeamInfo


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInfo
        fields = '__all__'
