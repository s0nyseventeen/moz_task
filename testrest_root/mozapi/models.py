from django.db import models


class Task(models.Model):
    task_id = models.IntegerField()
    task_url = models.CharField(max_length=255, null=True)  # !!! rm null=True

    def __str__(self):
        return f"{self.task_id}"
