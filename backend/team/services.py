# services.py
from .models import Team, TeamMember, Invitation, Project
from .tasks import send_invitation_email


class TeamService:
    @staticmethod
    def create_team(name, owner):
        return Team.objects.create(name=name, owner=owner)


class TeamMemberService:
    @staticmethod
    def add_member(team, user, display_role=None, role=None):
        return TeamMember.objects.create(
            team=team, user=user, display_role=display_role, role=role
        )


class InvitationService:
    @staticmethod
    def create_invitation(team, user):
        invitation = Invitation.objects.create(team=team, user=user)
        send_invitation_email(invitation)
        return invitation


class ProjectService:
    @staticmethod
    def create_project(
        name, team, creator, description=None, start_date=None, end_date=None
    ):
        return Project.objects.create(
            name=name,
            team=team,
            created_by=creator,
            description=description,
            start_date=start_date,
            end_date=end_date,
        )
