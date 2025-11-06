from rest_framework.viewsets import ModelViewSet

from .selectors import get_all_comment, get_all_tasks, get_all_attachments
from .serializers import TaskSerializer, CommentSerializer, AttachmentSerializer


class TaskViewSet(ModelViewSet):
    queryset = get_all_tasks()
    serializer_class = TaskSerializer


class CommentViewSet(ModelViewSet):
    queryset = get_all_comment()
    serializer_class = CommentSerializer


class AttachmentViewSet(ModelViewSet):
    queryset = get_all_attachments()
    serializer_class = AttachmentSerializer
