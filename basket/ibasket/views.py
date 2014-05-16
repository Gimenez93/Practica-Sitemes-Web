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
import os
from django.views.generic import CreateView, DetailView, ListView


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

def create(request,username):
	if request.method == 'POST':
		form = Comment(comment=request.POST['comment'], user=request.user, match=Match.objects.get(id=username))
		new_prova = form.save()
		return render(request, "thanks.html", {
		'id' : username,
		})
	else:
		f = open(os.path.join(os.path.dirname(__file__),'../basket/static/teams.json'),"r")
		json = f.read()
		form = ProvaForm(request.POST)
	return render(request, "create.html", {
		'form': form,
		'id' : username,
		"file": json
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



class MatchList(ListView):
	model = Match
	template_name = "matches.html"
	queryset = Match.objects.all()

class MatchDetail(DetailView):
	model = Match
	template_name = "match.html"
	queryset = Match.objects.all()

class TeamList(ListView):
	model = Team
	template_name = "teams.html"
	queryset = Team.objects.all()

class TeamDetail(DetailView):
	model = Team
	template_name = "team.html"
	queryset = Team.objects.all()

class PlayerList(ListView):
	model = Player
	template_name = "players.html"
	queryset = Player.objects.all()

class PlayerDetail(DetailView):
	model = Player
	template_name = "player.html"
	queryset = Player.objects.all()

class RefereeList(ListView):
	model = Referee
	template_name = "referees.html"
	queryset = Referee.objects.all()

class RefereeDetail(DetailView):
	model = Referee
	template_name = "referee.html"
	queryset = Referee.objects.all()

class UserList(ListView):
	model = User
	template_name = "users.html"
	queryset = User.objects.all()

class UserDetail(DetailView):
	model = User
	template_name = "user.html"
	queryset = User.objects.all() and Comment.objects.all()



