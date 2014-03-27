from django.contrib import admin
from ibasket.models import Match
from ibasket.models import Player
from ibasket.models import Referee
from ibasket.models import Comment
from ibasket.models import Team

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Referee)
admin.site.register(Comment)
