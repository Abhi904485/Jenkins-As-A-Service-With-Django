from django.db import models


class TeamInfo(models.Model):
    team_id = models.AutoField(primary_key=True, auto_created=True)
    team_name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.team_name

    def __str__(self):
        return self.team_name
