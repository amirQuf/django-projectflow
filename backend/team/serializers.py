from rest_framework.serializers import ModelSerializer
from .models import Team, TeamMember, Invitation, Project


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamMemberSerializer(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"


class InvitationSerializer(ModelSerializer):
    class Meta:
        model = Invitation
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
