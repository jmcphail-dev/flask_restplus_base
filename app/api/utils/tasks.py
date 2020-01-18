class Task:
    def __init__(self, name, details):
        self.name = name
        self.details = details

class TaskSet:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks else []

