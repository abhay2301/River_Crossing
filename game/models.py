from django.db import models

class HighScore(models.Model):
    player_name = models.CharField(max_length=100)
    moves = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)