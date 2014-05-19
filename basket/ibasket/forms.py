from django.forms import ModelForm
from ibasket.models import *


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ('user','match')

