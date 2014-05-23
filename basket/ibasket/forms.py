from django.forms import ModelForm
from django import forms
from ibasket.models import *


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ('user','match')


class TeamForm(ModelForm):
	class Meta:
		model = Team

class PlayerForm(ModelForm):
	class Meta:
		model = Player

class RefereeForm(ModelForm):
	class Meta:
		model = Referee

class MatchForm(ModelForm):
	class Meta:
		model = Match