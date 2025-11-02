from .models import Task, Comment, Attachment


def get_all_tasks():
    return Task.objects.all()


def get_all_comment():
    return Comment.objects.all()


def get_all_attachments():
    return Attachment.objects.all()
