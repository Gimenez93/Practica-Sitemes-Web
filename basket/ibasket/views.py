# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.shortcuts import render_to_response, render
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from ibasket.models import *



def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Basket aPP',
			'pagetitle': 'Welcome to the Basket aPPlication',
			'contentbody': 'Managing non legal funding since 2013',
			'user': request.user
		})
			



def userpage(request,username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	return render_to_response(
		'userpage.html',
		{
			'username': username,
			'comments': user.comment_set.all()
		})

def referee(request):
	return render_to_response(
		'referees.html',
		{
			'referees': Referee.objects.all()
		})

def referees(request, ref):
	try:
		referee = Referee.objects.get(id=ref)
	except:
		raise Http404('Referee not found.')

	return render_to_response(
		'referee.html',
		{
			'name': referee.name,
			'matches': referee.matches.all
		})

def players(request):
	#if(HttpRequest.META["QUERY_STRING"] == "xml"):
	#	data = serializers.serialize('xml', Players.objects.all())
	#	return HttpResponse(data, mimetype='application/xml')
	return render_to_response(
		'players.html',
		 {
			'players': Player.objects.all()
		})


def player(request, ref):
	try:
		player = Player.objects.get(id=ref)
	except:
		raise Http404('Player not found.')

	return render_to_response(
		'player.html',
		{
			'name': player.name,
			'age': player.age,
			'role': player.role,
			'team': player.team.name
		})

def teams(request):
	return render_to_response(
		'teams.html',
		 {
			'teams': Team.objects.all()
		})

def team(request, ref):
	try:
		team = Team.objects.get(id=ref)
	except:
		raise Http404('Team not found.')

	return render_to_response(
		'team.html',
		{
			'name': team.name,
			'year': team.year_fundation,
			'city': team.city,
			'coach': team.coach
		})

def matches(request):
	return render_to_response(
		'matches.html',
		 {
			'matches': Match.objects.all()
		})

def match(request, ref):
	try:
		match = Match.objects.get(id=ref)
	except:
		raise Http404('Match not found')

	return render_to_response(
		'match.html',
		{
			'local': match.localTeam,
			'visitant': match.visitantTeam,
			'visitantpoints': match.visitantScore,
			'localpoints': match.localScore,
			'id' : match.id,
		})

def comments(request, mat):
	return render_to_response(
		'comments.html',
		{
			'comments' : Comment.objects.filter(match=mat),
		})


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {
		'form': form,
		})


