from rest_framework import serializers
from to_do.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'title',
            'description',
            'completed',
            'created',
            'last_modification'
        )
        read_only_fields = (
            'created',
            'last_modification'
        )
