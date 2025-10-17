from rest_framework.viewsets import ModelViewSet


from .serializers import (
    TeamSerializer,
    TeamMemberSerializer,
    InvitationSerializer,
    ProjectSerializer,
)
from .models.team import Team
from .models.team_member import TeamMember
from .models.invitation import Invitation
from .models.project import Project


from rest_framework.response import Response


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
        serializer.save()
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
