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
	birth_place = models.TextField(max_length = 100)
	def __unicode__ (self):
		return self.name

class Match(models.Model):
	localTeam = models.ForeignKey(Team, related_name = 'localTeam')
	visitantTeam = models.ForeignKey(Team, related_name= 'visitantTeam')
	localScore = models.TextField(max_length = 3)
	visitantScore = models.TextField(max_length = 3)
	def __unicode__ (self):
		return self.localTeam.name + " - " + self.visitantTeam.name

	def averageRating(self):
		ratingSum = 0.0
		for comment in self.comment_set.all():
			ratingSum = ratingSum + comment.rating
		reviewCount = self.comment_set.count()
		return ratingSum/reviewCount




class Referee(models.Model):
	name = models.TextField(max_length = 100)
	matches = models.ManyToManyField(Match)
	def __unicode__ (self):
		return self.name

class Comment(models.Model):
	RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
	rating = models.PositiveSmallIntegerField('Ratings(stars)', blank=False, default=3, choices=RATING_CHOICES)
	user = models.ForeignKey(User)
	comment = models.TextField(max_length = 140)
	match = models.ForeignKey(Match)
	def __unicode__ (self):
		return self.comment


