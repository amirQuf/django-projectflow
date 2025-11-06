import pytest
from team.models.team import Team
from users.models import CustomUser


@pytest.mark.django_db
class TestTeamModel:
    def test_create_team(self):
        user = CustomUser.objects.create(username="testuser", email="user@example.com")
        team = Team.objects.create(name="Alpha", owner=user)

        assert team.name == "Alpha"
        assert team.owner == user
        assert team.created is not None
        assert team.modified is not None

    def test_ordering_meta(self):

        user = CustomUser.objects.create(username="order_user", email="o@example.com")
        team1 = Team.objects.create(name="First", owner=user)
        team2 = Team.objects.create(name="Second", owner=user)

        teams = list(Team.objects.all())
        assert teams[0].name == "Second"

    def test_modified_updates_on_save(self):
        user = CustomUser.objects.create(username="mod_user", email="m@example.com")
        team = Team.objects.create(name="Editable", owner=user)

        old_modified = team.modified
        team.name = "Edited Name"
        team.save()

        team.refresh_from_db()
        assert team.modified > old_modified
