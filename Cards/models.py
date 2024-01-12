from django.db import models

# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DOB = models.DateField()
    height = models.FloatField()
    country = models.CharField(max_lenth=100)


class Stats(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    three_pt = models.FloatField()
    ppg = models.FloatField()
    rpg = models.FloatField()
    apg = models.FloatField()
    stlpg = models.FloatField()
