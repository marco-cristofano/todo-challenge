from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from to_do.models import ToDo
from to_do.serializers.to_do import ToDoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    @action(detail=True, methods=['put'], url_path='completed')
    def completed(self, request, pk=None):
        to_do = self.get_object()
        to_do.set_completed()
        return Response(self.serializer_class(to_do).data)
