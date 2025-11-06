from team.models.team import Team
import pytest
from users.models import CustomUser
from team.models.team_member import TeamMember

from django.utils import timezone


@pytest.mark.django_db
class TestTeamMemberModel:

    @pytest.fixture
    def setup_data(self):
        user1 = CustomUser.objects.create_user(username="user1", password="pass123")
        user2 = CustomUser.objects.create_user(username="user2", password="pass123")
        team = Team.objects.create(name="Test Team", owner=user1)
        member = TeamMember.objects.create(team=team, user=user2, role=1)
        return {"user1": user1, "user2": user2, "team": team, "member": member}

    def test_team_member_creation(self, setup_data):
        member = setup_data["member"]
        assert member.id is not None
        assert member.role == 1
        assert member.team.name == "Test Team"
        assert member.user.username == "user2"

    def test_joined_at_auto_now_add(self, setup_data):
        member = setup_data["member"]
        assert member.joined_at is not None
        assert abs((timezone.now() - member.joined_at).total_seconds()) < 5

    def test_display_role_member(self, setup_data):
        member = setup_data["member"]
        assert member.display_role() == "MEMBER"

    def test_display_role_admin(self, setup_data):
        member = setup_data["member"]
        member.role = 2
        assert member.display_role() == "ADMIN"

    def test_display_role_manager(self, setup_data):
        member = setup_data["member"]
        member.role = 3
        assert member.display_role() == "MANAGER"

    def test_str_representation(self, setup_data):
        member = setup_data["member"]
        expected_str = f"{member.user}({member.role}) | {member.team}"
        assert str(member) == expected_str

    def test_meta_ordering(self, setup_data):
        team = setup_data["team"]
        user3 = CustomUser.objects.create_user(username="user3", password="pass123")
        member2 = TeamMember.objects.create(team=team, user=user3, role=1)
        members = list(TeamMember.objects.all())
        assert members[0] == member2
        assert members[1] == setup_data["member"]
