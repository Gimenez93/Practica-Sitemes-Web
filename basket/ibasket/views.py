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
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied




class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
	def get_object(self, *args, **kwargs):
		obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
		if not obj.user == self.request.user:
			raise PermissionDenied
		return obj

class CheckIsStaffMixin(object):
	def get_object(self, *args, **kwargs):
		obj = super(CheckIsStaffMixin, self).get_object(*args, **kwargs)
		if not self.request.user.is_staff:
			raise PermissionDenied
		return obj	



def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Basket aPP',
			'pagetitle': 'Benvingut a la aPP de basket!',
			'contentbody': 'La millor aPP per consultar el teu esport favorit, basket!',
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

class MatchList(LoginRequiredMixin, ListView):
	model = Match
	template_name = "matches.html"
	queryset = Match.objects.all()

class MatchDetail(LoginRequiredMixin, DetailView):
	model = Match
	template_name = "match.html"

class TeamList(LoginRequiredMixin, ListView):
	model = Team
	template_name = "teams.html"
	queryset = Team.objects.all()

class TeamDetail(LoginRequiredMixin, DetailView):
	model = Team
	template_name = "team.html"

class PlayerList(LoginRequiredMixin, ListView):
	model = Player
	template_name = "players.html"
	queryset = Player.objects.all()

class PlayerDetail(LoginRequiredMixin, DetailView):
	model = Player
	template_name = "player.html"

class RefereeList(LoginRequiredMixin, ListView):
	model = Referee
	template_name = "referees.html"
	queryset = Referee.objects.all()

class RefereeDetail(LoginRequiredMixin, DetailView):
	model = Referee
	template_name = "referee.html"

class UserList(LoginRequiredMixin, ListView):
	model = User
	template_name = "users.html"
	queryset = User.objects.all()

class UserDetail(LoginRequiredMixin, DetailView):
	model = User
	template_name = "user.html"


class CreateComment(LoginRequiredMixin, CreateView):
	model = Comment
	template_name = "form.html"
	form_class = CommentForm
	success_url = "/matches/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.match = Match.objects.get(id=self.kwargs['pk'])
		return super(CreateComment, self).form_valid(form)



class UpdateComment(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = "form.html"
	success_url = "/matches/"
	
class DeleteComment(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
	model = Comment
	success_url = "/matches/"
	template_name = "form_delete.html"

class CreateTeam(LoginRequiredMixin, CreateView):
	model = Team
	template_name = "form.html"
	form_class = TeamForm
	success_url = "/teams/"

class UpdateTeam(LoginRequiredMixin, CheckIsStaffMixin, UpdateView):
	model = Team
	form_class = TeamForm
	template_name = "form.html"
	success_url = "/teams/"
	
class DeleteTeam(LoginRequiredMixin, CheckIsStaffMixin, DeleteView):
	model = Team
	success_url = "/teams/"
	template_name = "form_delete.html"

class CreatePlayer(LoginRequiredMixin, CreateView):
	model = Player
	template_name = "form.html"
	form_class = PlayerForm
	success_url = "/players/"

class UpdatePlayer(LoginRequiredMixin, CheckIsStaffMixin, UpdateView):
	model = Player
	form_class = PlayerForm
	template_name = "form.html"
	success_url = "/players/"
	
class DeletePlayer(LoginRequiredMixin, CheckIsStaffMixin, DeleteView):
	model = Player
	success_url = "/players/"
	template_name = "form_delete.html"

class CreateReferee(LoginRequiredMixin, CreateView):
	model = Referee
	template_name = "form.html"
	form_class = RefereeForm
	success_url = "/referees/"

class UpdateReferee(LoginRequiredMixin, CheckIsStaffMixin, UpdateView):
	model = Referee
	form_class = RefereeForm
	template_name = "form.html"
	success_url = "/referees/"
	
class DeleteReferee(LoginRequiredMixin, CheckIsStaffMixin, DeleteView):
	model = Referee
	success_url = "/referees/"
	template_name = "form_delete.html"	

class CreateMatch(LoginRequiredMixin, CreateView):
	model = Match
	template_name = "form.html"
	form_class = MatchForm
	success_url = "/matches/"

class UpdateMatch(LoginRequiredMixin, CheckIsStaffMixin, UpdateView):
	model = Match
	form_class = MatchForm
	template_name = "form.html"
	success_url = "/matches/"
	
class DeleteMatch(LoginRequiredMixin, CheckIsStaffMixin, DeleteView):
	model = Match
	success_url = "/matches/"
	template_name = "form_delete.html"	

