from .models.project import Project
from django.utils import timezone
from .models.invitation import Invitation
from .models.team import Team
from .models.team_member import TeamMember


def find_team_project(team_id: int):
    """
    finding project of the specific time by team_id
    returning project as querysets
    """
    qs = Project.objects.filter(team=team_id)
    return qs


def get_all_teams():
    qs = Team.objects.all()
    return qs


def get_all_team_member():
    return TeamMember.objects.all()


def get_all_Invitation():
    qs = Invitation.objects.all()
    return qs


def get_all_project():
    qs = Project.objects.all()
    return qs


def find_expired_invitations():
    """
    find expired invitations that noe is expired for set their status
    """
    invitations = Invitation.objects.filter(expires_at__lt=timezone.now())

    return invitations
