from django.contrib import admin

from .models.team import Team
from .models.team_member import TeamMember
from .models.invitation import Invitation
from .models.project import Project


admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Invitation)
admin.site.register(Project)
