from django.db import models


class Task(models.Model):
    task_id = models.IntegerField()

    def __str__(self):
        return f"{self.task_id}"
