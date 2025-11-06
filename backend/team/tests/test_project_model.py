import pytest
from users.models import CustomUser
from team.models.project import Project
from team.models.team import Team
from django.utils import timezone


@pytest.mark.django_db
class TestProjectModel:

    @pytest.fixture
    def setup_data(self):
        user = CustomUser.objects.create_user(username="creator", password="test123")
        owner = CustomUser.objects.create_user(username="owner", password="test123")
        team = Team.objects.create(name="Dev Team", owner=owner)
        project = Project.objects.create(
            name="Backend API",
            description="Develop RESTful API using Django REST Framework",
            team=team,
            status=Project.Status.ACTIVE,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=7),
            created_by=user,
        )
        return {"user": user, "team": team, "project": project}

    def test_project_creation(self, setup_data):
        project = setup_data["project"]
        assert project.id is not None
        assert project.name == "Backend API"
        assert project.status == Project.Status.ACTIVE
        assert project.team.name == "Dev Team"
        assert project.created_by.username == "creator"

    def test_default_status(self, setup_data):
        team = setup_data["team"]
        user = setup_data["user"]
        project = Project.objects.create(
            name="Default Status Project",
            description="Testing default status",
            team=team,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=3),
            created_by=user,
        )
        assert project.status == Project.Status.ACTIVE

    def test_str_representation(self, setup_data):
        project = setup_data["project"]
        assert str(project) == "Backend API"

    def test_meta_ordering(self, setup_data):
        team = setup_data["team"]
        user = setup_data["user"]

        p1 = setup_data["project"]
        p2 = Project.objects.create(
            name="Frontend UI",
            description="Create frontend with React",
            team=team,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=14),
            created_by=user,
        )

        projects = list(Project.objects.all())
        assert projects[0] == p2
        assert projects[1] == p1

    def test_date_fields(self, setup_data):
        project = setup_data["project"]
        assert project.start_date < project.end_date
        assert abs((timezone.now() - project.created_at).total_seconds()) < 5

    def test_status_choices(self):
        assert Project.Status.ACTIVE == "Ac"
        assert Project.Status.ARCHIVED == "Ar"
        assert Project.Status.COMPLETED == "C"
