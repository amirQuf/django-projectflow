from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    PrimaryKeyRelatedField,
)
from .models import Team, TeamMember, Invitation, Project


from .services import send_invitation_email, invite_user
from users.serializers import CustomUserSerializer
from users.models import CustomUser


class TeamSerializer(ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    owner_id = PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )

    def create(self, validated_data):
        owner = validated_data.pop("owner_id")
        team = Team.objects.create(owner=owner, **validated_data)
        return team

    class Meta:
        model = Team
        fields = ["id", "name", "owner", "owner_id", "created", "modified"]


class TeamMemberSerializer(ModelSerializer):
    team = TeamSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)

    team_id = PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True)

    class Meta:
        model = TeamMember
        fields = ["id", "team", "user", "role", "joined_at"]


class InvitationSerializer(ModelSerializer):
    team = TeamSerializer(read_only=True)
    status_display = CharField(read_only=True, source="get_status_display")

    def create(self, validated_data):
        invitation = super().create(validated_data)
        send_invitation_email(invitation)
        return invitation

    class Meta:
        model = Invitation
        fields = [
            "id",
            "team",
            # "team_obj",
            "email",
            "token",
            "status",
            "status_display",
            "created_at",
            "expires_at",
            "invite_link",
        ]


class ProjectSerializer(ModelSerializer):
    team_obj = TeamSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "team",
            "team_obj",
            "start_date",
            "end_date",
            "created_by",
            "created_at",
        ]
