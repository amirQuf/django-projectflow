from rest_framework.viewsets import ModelViewSet
from .models import Team, TeamMember, Invitation, Project
from .serializers import (
    TeamSerializer,
    TeamMemberSerializer,
    InvitationSerializer,
    ProjectSerializer,
)

from rest_framework.response import Response
from .services import send_invitation_email


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMemberViewSet(ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class InvitationViewSet(ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def create(self, request):

        serializer = InvitationSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        invitation = serializer.save()
        return Response(
            {
                "type": "success",
                "message": "Email has sent.",
                "result": {serializer.validated_data},
            }
        )


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
