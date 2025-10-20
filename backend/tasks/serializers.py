from .models import Task, Comment


from rest_framework import serializers

from team.serializers import ProjectSerializer
from users.serializers import CustomUserSerializer
from users.models import CustomUser
from team.models.project import Project


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), write_only=True
    )
    assigned_to = CustomUserSerializer(read_only=True)
    worker_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )
    created_by = CustomUserSerializer(read_only=True)
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )

    def create(self, validated_data):
        creator = validated_data.pop("creator_id")
        worker = validated_data.pop("worker_id")
        project = validated_data.pop("project_id")
        project = Task.objects.create(
            created_by=creator, assigned_to=worker, project=project, **validated_data
        )
        return project

    class Meta:
        model = Task
        fields = [
            "project",
            "title",
            "description",
            "assigned_to",
            "priority",
            "status",
            "due_date",
            "created_at",
            "updated_at",
            "created_by",
        ]


class CommentSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    task_id = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), write_only=True
    )

    user = CustomUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )

    def create(self, validated_data):
        user = validated_data.pop("user_id")
        task = validated_data.pop("task_id")
        comment = Comment.object.create(user=user, task=task)

        return comment

    class Meta:
        model = Comment
        fields = ["task", "user", "content", "created_at"]
