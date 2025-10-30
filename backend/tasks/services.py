from .model import Task, Comment


def create_task(*args, **kwargs) -> Task:
    task = Task, object.create(*args, **kwargs)
    return task
