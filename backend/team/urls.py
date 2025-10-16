from rest_framework.routers import SimpleRouter
from .views import TeamViewSet, TeamMemberViewSet, InvitationViewSet, ProjectViewSet

router = SimpleRouter()
router.register("team", TeamViewSet)
router.register("teammeber", TeamMemberViewSet)
router.register("invite", InvitationViewSet)
router.register("project", ProjectViewSet)

urlpatterns = router.urls
