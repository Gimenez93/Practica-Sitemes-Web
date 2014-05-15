from django.forms import ModelForm
from ibasket.models import Comment
from ibasket.models import Prova


class CommentForm(ModelForm):
	class Meta:
		model = Comment

class ProvaForm(ModelForm):
	class Meta:
		model = Prova
		exclude = ['user' , 'match']
