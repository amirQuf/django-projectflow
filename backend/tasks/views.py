from rest_framework.viewsets import ModelViewSet

from .selectors import get_all_comment, get_all_tasks
from .serializers import TaskSerializer, CommentSerializer


class TaskViewSet(ModelViewSet):
    query_set = get_all_tasks()
    serializer_class = TaskSerializer


class CommentViewSet(ModelViewSet):
    query_set = get_all_comment()
    serializer_class = CommentSerializer
