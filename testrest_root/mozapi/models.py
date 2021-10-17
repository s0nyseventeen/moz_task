from django.db import models


class Task(models.Model):
    # task_id = models.IntegerField()
    task_url = models.CharField(verbose_name='url', max_length=255)

    # rm null=True; automatically set time to now if we don't specify the time
    created_on = models.DateTimeField(auto_now_add=True, null=True)  
    user = ...  # need to create User model

    def __str__(self):
        return f"{self.task_url}"
