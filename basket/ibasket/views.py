# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from ibasket.models import Referee


def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Basket aPP',
		'pagetitle': 'Welcome to the Basket aPPlication',
		'contentbody': 'Managing non legal funding since 2013'
	})
	output = template.render(variables)
	return HttpResponse(output)

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	comments = user.comment_set.all()
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'comments': comments
	})
	output = template.render(variables)
	return HttpResponse(output)


def referee(request):
	referees = Referee.objects.all()
	template = get_template('referees.html')
	variables = Context({
		'referee': referees
	})
	output = template.render(variables)
	return HttpResponse(output)


def referees(request, ref):
	try:
		referee = Referee.objects.get(name=ref)
	except:
		raise Http404('Referee not found.')
	template = get_template('referee.html')
	variables = Context({
		'name': referee.name,
		'matches': referee.matches.all
	})
	output = template.render(variables)
	return HttpResponse(output)
	
def team(request):
	team = Team.objects.all()
	template = get_template('teams.html')
	variables = Context({
		'team': teams
	})
	output = template.render(variables)
	return HttpResponse(output)


def teams(request, te):
	try:
		team = Team.objects.get(name=te)
	except:
		raise Http404('Team not found.')
	template = get_template('team.html')
	variables = Context({
		'name': team.name,
		'coach': team.coach,
		'city': team.city,
		'year_fundation': team.year_fundation,
#		'matches': referee.matches.all
	})
	output = template.render(variables)
	return HttpResponse(output)
	
def player(request):
	playerss = Player.objects.all()
	template = get_template('players.html')
	variables = Context({
		'player': players
	})
	output = template.render(variables)
	return HttpResponse(output)


def players(request, pla):
	try:
		player = Player.objects.get(name=pla)
	except:
		raise Http404('Player not found.')
	template = get_template('player.html')
	variables = Context({
		'name': player.name,
		'age': player.age,
		'role': player.role,
		'team': player.team,
#		'matches': referee.matches.all
	})
	output = template.render(variables)
	return HttpResponse(output)
	
def comment(request):
	comments = Comment.objects.all()
	template = get_template('comments.html')
	variables = Context({
		'comment': comments
	})
	output = template.render(variables)
	return HttpResponse(output)


def comments(request, com):
	try:
		comment = Comment.objects.get(name=com)
	except:
		raise Http404('Comment not found.')
	template = get_template('comment.html')
	variables = Context({
		'user': Comment.user,
		'comment': Comment.comment,
		'match': Comment.match,
#		'matches': referee.matches.all
	})
	output = template.render(variables)
	return HttpResponse(output)

def match(request):
	matches = Match.objects.all()
	template = get_template('matches.html')
	variables = Context({
		'match': matches
	})
	output = template.render(variables)
	return HttpResponse(output)


def matches(request, mat):
	try:
		match = Match.objects.get(name=mat)
	except:
		raise Http404('Match not found.')
	template = get_template('match.html')
	variables = Context({
		'localTeam': Match.localTeam,
		'visitantTeam': Match.visitamtTeam,
		'localScore': Match.localScore,
		'visitantScore': Match.visitantScore,
#		'matches': referee.matches.all
	})
	output = template.render(variables)
	return HttpResponse(output)

