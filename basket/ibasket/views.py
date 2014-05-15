# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.shortcuts import render_to_response, render
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from ibasket.models import *
from ibasket.forms import *



def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Basket aPP',
			'pagetitle': 'Welcome to the Basket aPPlication',
			'contentbody': 'The best aPP for consult your favourite sport, basket!',
			'user': request.user
		})
			



def userpage(request,username):
	try:
		user = User.objects.get(id=username)
	except:
		raise Http404('User not found.')

	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", User.objects.filter(id=username))
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", User.objects.filter(id=username))
		return HttpResponse(data, mimetype='application/json')

	return render_to_response(
		'userpage.html',
		{
			'username': user.username,
			'comments': user.comment_set.all(),
			'user': request.user,
		})

def users(request):
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", User.objects.all())
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", User.objects.all())
		return HttpResponse(data, mimetype='application/json')
	return render_to_response(
		'users.html',
		{
			'users': User.objects.all(),
			'user': request.user,
		})


def referee(request):
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Referee.objects.all())
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Referee.objects.all())
		return HttpResponse(data, mimetype='application/json')
	return render_to_response(
		'referees.html',
		{
			'referees': Referee.objects.all(),
			'user': request.user
		})

def referees(request, ref):
	try:
		referee = Referee.objects.get(id=ref)
	except:
		raise Http404('Referee not found.')

	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Referee.objects.filter(id=ref))
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Referee.objects.filter(id=ref))
		return HttpResponse(data, mimetype='application/json')

	return render_to_response(
		'referee.html',
		{
			'name': referee.name,
			'matches': referee.matches.all,
			'user': request.user,
		})

def players(request):
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Player.objects.all())
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Player.objects.all())
		return HttpResponse(data, mimetype='application/json')
	return render_to_response(
		'players.html',
		 {
			'players': Player.objects.all(),
			'user': request.user,
		})


def player(request, ref):
	try:
		player = Player.objects.get(id=ref)
	except:
		raise Http404('Player not found.')
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Player.objects.filter(id=ref))
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Player.objects.filter(id=ref))
		return HttpResponse(data, mimetype='application/json')

	return render_to_response(
		'player.html',
		{
			'name': player.name,
			'age': player.age,
			'role': player.role,
			'team': player.team.name,
			'user': request.user,
		})

def teams(request):
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Team.objects.all())
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Team.objects.all())
		return HttpResponse(data, mimetype='application/json')
	return render_to_response(
		'teams.html',
		 {
			'teams': Team.objects.all(),
			'user': request.user,
		})

def team(request, ref):
	try:
		team = Team.objects.get(id=ref)
	except:
		raise Http404('Team not found.')
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", teamIterable)
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", teamIterable)
		return HttpResponse(data, mimetype='application/json')

	return render_to_response(
		'team.html',
		{
			'name': team.name,
			'year': team.year_fundation,
			'city': team.city,
			'coach': team.coach,
			'user': request.user,
		})

def matches(request):
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Match.objects.all())
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Match.objects.all())
		return HttpResponse(data, mimetype='application/json')
	return render_to_response(
		'matches.html',
		 {
			'matches': Match.objects.all(),
			'user': request.user,
		})

def match(request, ref):
	try:
		match = Match.objects.get(id=ref)
	
	except:
		raise Http404('Match not found')
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Match.objects.filter(id=ref))
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Match.objects.filter(id=ref))
		return HttpResponse(data, mimetype='application/json')

	return render_to_response(
		'match.html',
		{
			'local': match.localTeam,
			'visitant': match.visitantTeam,
			'visitantpoints': match.visitantScore,
			'localpoints': match.localScore,
			'id' : match.id,
			'user': request.user,
		})

def comments(request, mat):
	if request.META["QUERY_STRING"] == "xml":
		data = serializers.serialize("xml", Comment.objects.all())
		return HttpResponse(data, mimetype='application/xml')
	if request.META["QUERY_STRING"] == "json":
		data = serializers.serialize("json", Comment.objects.all())
		return HttpResponse(data, mimetype='application/json')
	return render_to_response(
		'comments.html',
		{
			'comments' : Comment.objects.filter(match=mat),
			'match' : Match.objects.get(id=mat),
			'user': request.user,
			'id': mat
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


def prova(request):
	if request.method == 'POST':
		form = Prova(name=request.POST['name'],lastname=request.POST['lastname'],)
		new_prova = form.save()
		return HttpResponseRedirect("/")
	else:
		form = ProvaForm(request.POST)
	return render(request, "prova.html", {
		'form': form,
		})

def create(request,username):
	if request.method == 'POST':
		form = Comment(comment=request.POST['comment'], user=request.user, match=Match.objects.get(id=username))
		new_prova = form.save()
		return render(request, "thanks.html", {
		'id' : username,
		})
	else:
		form = ProvaForm(request.POST)
	return render(request, "create.html", {
		'form': form,
		'id' : username
		})

def edit(request,match,idComment):
	if request.method == 'POST':
		form = Comment.objects.get(id=idComment)
		form.comment = request.POST['comment']
		new_prova = form.save()
		return render(request, "thanks.html", {
		'id' : match,
		})
	else:
		comment = Comment.objects.get(id=idComment)
		form = ProvaForm(request.POST,comment)
	return render(request, "edit.html", {
		'form': form,
		'idComment' : idComment,
		'idMatch' : match,
		'comment' : comment,
		})

def delete(request,match,idComment):
	form = Comment.objects.get(id=idComment)
	form.delete()
	return render(request, "thanks.html", {
	'id' : match,
	})
