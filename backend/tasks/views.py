from rest_framework.viewsets import ModelViewSet

from .selectors import get_all_comment, get_all_tasks, get_all_attachments
from .serializers import TaskSerializer, CommentSerializer, AttachmentSerializer

from .models import Task, Comment, Attachment


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AttachmentViewSet(ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
