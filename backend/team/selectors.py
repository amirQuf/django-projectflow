from .models.project import Project
from django.utils import timezone
from .models.invitation import Invitation


def find_team_project(team_id: int):
    """
    finding project of the specific time by team_id
    returning project as querysets
    """
    qs = Project.objects.filter(team=team_id)
    return qs


def find_expired_invitations():
    """
    find expired invitations that noe is expired for set their status
    """
    invitations = Invitation.objects.filter(expires_at__lt=timezone.now())

    return invitations
