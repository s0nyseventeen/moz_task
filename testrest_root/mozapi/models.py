from django.db import models


class Task(models.Model):
    #task_id = models.IntegerField()
    task_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.task_url}"
