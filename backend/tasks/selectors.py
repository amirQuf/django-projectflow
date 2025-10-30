from .models import Task, Comment


def get_all_tasks():
    return Task.objects.all()


def get_all_comment():
    return Comment.objects.all()
