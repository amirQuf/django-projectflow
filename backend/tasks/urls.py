from rest_framework.router import SimpleRouter


from .views import TaskViewSet, CommentViewSet, AttachmentViewSet

router = SimpleRouter()
router.register("task", TaskViewSet)
router.register("comment", CommentViewSet)
router.register("attachment", AttachmentViewSet)

url_patterns = router.urls
