from rest_framework import serializers

from .models.team import Team
from .models.team_member import TeamMember
from .models.invitation import Invitation
from .models.project import Project


from .tasks import send_invitation_email

from users.serializers import CustomUserSerializer
from users.models import CustomUser


class TeamSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )

    def create(self, validated_data):
        owner = validated_data.pop("owner_id")
        team = Team.objects.create(owner=owner, **validated_data)
        return team

    class Meta:
        model = Team
        fields = ["id", "name", "owner", "owner_id", "created", "modified"]


class TeamMemberSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), write_only=True
    )

    def create(self, validated_data):
        team = validated_data.pop("team_id")
        user = validated_data.pop("user_id")
        teammember = TeamMember.objects.create(team=team, user=user, **validated_data)
        return teammember

    class Meta:
        model = TeamMember
        fields = [
            "id",
            "team",
            "team_id",
            "user_id",
            "user",
            "display_role",
            "role",
            "joined_at",
        ]


class InvitationSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    status_display = serializers.CharField(read_only=True, source="get_status_display")
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), write_only=True
    )

    def create(self, validated_data):
        team = validated_data.pop("team_id")
        user = validated_data.pop("user_id")

        invitation = Invitation.objects.create(team=team, user=user, **validated_data)
        send_invitation_email.delay(invitation)
        return invitation

    class Meta:
        model = Invitation
        fields = [
            "id",
            "team",
            "team_id",
            "user",
            "user_id",
            "token",
            "status",
            "status_display",
            "created_at",
            "expires_at",
            "invite_link",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), write_only=True
    )

    def create(self, validated_data):
        team = validated_data.pop("team_id")
        creator = validated_data.pop("creator_id")
        project = Project.objects.create(
            team=team, created_by=creator, **validated_data
        )
        return project

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "team",
            "team_id",
            "start_date",
            "end_date",
            "created_by",
            "creator_id",
            "created_at",
        ]
