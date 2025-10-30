from rest_framework.viewsets import ModelViewSet


from .renderers import CustomRenderer

from .serializers import (
    TeamSerializer,
    TeamMemberSerializer,
    InvitationSerializer,
    ProjectSerializer,
)


from rest_framework.response import Response
from .selectors import (
    get_all_teams,
    get_all_team_member,
    get_all_Invitation,
    get_all_project,
)


class TeamViewSet(ModelViewSet):
    queryset = get_all_teams()
    serializer_class = TeamSerializer


class TeamMemberViewSet(ModelViewSet):
    queryset = get_all_team_member()
    serializer_class = TeamMemberSerializer


class InvitationViewSet(ModelViewSet):
    queryset = get_all_Invitation()
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
                "result": {**serializer.data},
            }
        )


class ProjectViewSet(ModelViewSet):
    queryset = get_all_project()
    serializer_class = ProjectSerializer
