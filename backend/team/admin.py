from django.contrib import admin
from .models import Team, TeamMember, Invitation, Project

admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Invitation)
admin.site.register(Project)
