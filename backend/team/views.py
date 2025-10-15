from rest_framework.viewsets import ModelViewSet
from .models import Team, TeamMember, Invitation, Project
from .serializers import (
    TeamSerializer,
    TeamMemberSerializer,
    InvitationSerializer,
    ProjectSerializer,
)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMemberViewSet(ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class InvitationViewSet(ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
