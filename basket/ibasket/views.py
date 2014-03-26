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
		raise Http404('User not found.')
	template = get_template('referee.html')
	variables = Context({
		'name': referee.name,
		'matches': referee.matches.all
	})
	output = template.render(variables)
	return HttpResponse(output)

