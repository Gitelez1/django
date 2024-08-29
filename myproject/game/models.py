from django.db import models

# Create your models here.

class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    attempts = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.attempts} attempts"