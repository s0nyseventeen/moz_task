from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def create(self, validated_data):
        """Create and return a new Task
        """
        newtask = Task(
            # task_id=validate_data['task_id'],
            task_url=validated_data['task_url']
        )
        newtask.save()
        return newtask
