from team.models.team import Team
import pytest

from users.models import CustomUser

from team.models.invitation import Invitation
from django.utils import timezone, timedelta


@pytest.mark.django_db
class TestInvitationModel:

    @pytest.fixture
    def setup_data(self):
        inviter = CustomUser.objects.create_user(username="owner", password="1234")
        invited_user = CustomUser.objects.create_user(username="guest", password="1234")
        team = Team.objects.create(name="Core Team", owner=inviter)
        invitation = Invitation.objects.create(
            user=invited_user,
            team=team,
        )
        return {
            "inviter": inviter,
            "invited_user": invited_user,
            "team": team,
            "invitation": invitation,
        }

    def test_invitation_creation(self, setup_data):
        invitation = setup_data["invitation"]
        assert invitation.id is not None
        assert invitation.status == Invitation.Status.PENDING
        assert invitation.token is not None
        assert len(str(invitation.token)) > 5

    def test_default_expiry_date(self, setup_data):
        invitation = setup_data["invitation"]
        diff = invitation.expires_at - timezone.now()
        assert 2.9 < diff.days < 3.1 or diff > timedelta(days=2, hours=23)

    def test_invitation_str(self, setup_data):
        invitation = setup_data["invitation"]
        assert str(invitation)

    def test_invitation_link(self, setup_data):
        invitation = setup_data["invitation"]
        link = invitation.invite_link()
        assert link.startswith("https://yourapp.com/invite/")
        assert str(invitation.token) in link

    def test_status_choices(self):
        assert Invitation.Status.PENDING == "P"
        assert Invitation.Status.ACCEPTED == "A"
        assert Invitation.Status.EXPIRED == "E"

    def test_meta_ordering(self, setup_data):
        team = setup_data["team"]
        user = setup_data["invited_user"]

        inv1 = setup_data["invitation"]
        inv2 = Invitation.objects.create(user=user, team=team)
        invitations = list(Invitation.objects.all())
        assert invitations[0] == inv2
        assert invitations[1] == inv1

    def test_can_expire_manually(self, setup_data):
        invitation = setup_data["invitation"]
        invitation.status = Invitation.Status.EXPIRED
        invitation.save()
        assert invitation.status == Invitation.Status.EXPIRED
