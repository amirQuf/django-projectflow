from rest_framework.routers import SimpleRouter


from .views import TaskViewSet, CommentViewSet, AttachmentViewSet


router = SimpleRouter()
router.register("task", TaskViewSet)
router.register("comment", CommentViewSet)
router.register("attachment", AttachmentViewSet)

urlpatterns = router.urls
