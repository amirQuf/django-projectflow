from rest_framework.router import SimpleRouter


from .views import TaskViewSet, CommentViewSet

router = SimpleRouter()
router.register("task", TaskViewSet)
router.register("comment", CommentViewSet)


url_patterns = router.urls
