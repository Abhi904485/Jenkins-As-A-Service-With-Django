from django.db import models

from team.models import TeamInfo


class VolumeInfo(models.Model):
    volume_id = models.AutoField(primary_key=True, auto_created=True)
    team_name = models.ForeignKey(TeamInfo, models.CASCADE)
    volume_name = models.CharField(max_length=100)

    def __repr__(self):
        return self.volume_name

    def __str__(self):
        return self.volume_name
