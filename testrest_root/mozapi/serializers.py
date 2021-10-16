from rest_framework import serializers
from .models import Task


#class TaskSerializer(serializers.Serializer):
#    task_id = serializers.IntegerField()
#    task_url = serializers.CharField(max_length=255)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "task_id"
        ]
