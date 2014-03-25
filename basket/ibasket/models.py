from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.TextField(max_length = 100)
	coach = models.TextField(max_length = 100)
	city = models.TextField(max_length = 100)
	year_fundation = models.IntegerField(max_length = 4)

class Player(models.Model):
	name = models.TextField(max_length = 100)
	age = models.IntegerField(max_length = 2)
	role = models.TextField(max_length = 100)
	team = models.ForeignKey(Team)

class Match(models.Model):
	localTeam = models.ForeignKey(Team, related_name = 'localTeam')
	visitantTeam = models.ForeignKey(Team, related_name= 'visitantTeam')
	localScore = models.IntegerField(max_length = 3)
	visitantScore = models.IntegerField(max_length = 3)
	
