from django.db import models

# Create your models here.
from team.models import TeamInfo
from volume.models import VolumeInfo


class ServiceInfo(models.Model):
    service_id = models.AutoField(primary_key=True, auto_created=True)
    team_name = models.ForeignKey(TeamInfo, on_delete=models.CASCADE)
    volume_name = models.ForeignKey(VolumeInfo, on_delete=models.CASCADE)
    database_url = models.CharField(max_length=200)
    virtual_service_url = models.CharField(max_length=100, unique=True)
    virtual_service = models.CharField(max_length=100, unique=True)
    database_name = models.CharField(max_length=100, unique=True)
    service_name = models.CharField(max_length=200, unique=False)

    def __repr__(self):
        return self.team_name

    def __str__(self):
        return self.team_name.team_name
