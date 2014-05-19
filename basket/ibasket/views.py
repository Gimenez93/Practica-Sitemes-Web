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
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Basket aPP',
			'pagetitle': 'Welcome to the Basket aPPlication',
			'contentbody': 'The best aPP for consult your favourite sport, basket!',
			'user': request.user
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

class MatchList(ListView):
	model = Match
	template_name = "matches.html"
	queryset = Match.objects.all()

class MatchDetail(DetailView):
	model = Match
	template_name = "match.html"

class TeamList(ListView):
	model = Team
	template_name = "teams.html"
	queryset = Team.objects.all()

class TeamDetail(DetailView):
	model = Team
	template_name = "team.html"

class PlayerList(ListView):
	model = Player
	template_name = "players.html"
	queryset = Player.objects.all()

class PlayerDetail(DetailView):
	model = Player
	template_name = "player.html"

class RefereeList(ListView):
	model = Referee
	template_name = "referees.html"
	queryset = Referee.objects.all()

class RefereeDetail(DetailView):
	model = Referee
	template_name = "referee.html"

class UserList(ListView):
	model = User
	template_name = "users.html"
	queryset = User.objects.all()

class UserDetail(DetailView):
	model = User
	template_name = "user.html"


class CreateComment(CreateView):
	model = Comment
	template_name = "form.html"
	form_class = CommentForm
	success_url = "/matches/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.match = Match.objects.get(id=self.kwargs['pk'])
		return super(CreateComment, self).form_valid(form)

class UpdateComment(UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = "form.html"
	success_url = "/matches/"
	
class DeleteComment(DeleteView):
	model = Comment
	success_url = "/matches/"
	template_name = "form.html"
