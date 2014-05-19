from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
	name = models.TextField(max_length = 100)
	coach = models.TextField(max_length = 100)
	city = models.TextField(max_length = 100)
	year_fundation = models.IntegerField(max_length = 4)
	def __unicode__ (self):
		return self.name

class Player(models.Model):
	name = models.TextField(max_length = 100)
	age = models.IntegerField(max_length = 2)
	role = models.TextField(max_length = 100)
	team = models.ForeignKey(Team)
	def __unicode__ (self):
		return self.name

class Match(models.Model):
	localTeam = models.ForeignKey(Team, related_name = 'localTeam')
	visitantTeam = models.ForeignKey(Team, related_name= 'visitantTeam')
	localScore = models.TextField(max_length = 3)
	visitantScore = models.TextField(max_length = 3)
	def __unicode__ (self):
		return self.localTeam.name + " - " + self.visitantTeam.name

class Referee(models.Model):
	name = models.TextField(max_length = 100)
	matches = models.ManyToManyField(Match)
	def __unicode__ (self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey(User)
	comment = models.TextField(max_length = 140)
	match = models.ForeignKey(Match)
	def __unicode__ (self):
		return self.comment


