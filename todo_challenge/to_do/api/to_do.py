from rest_framework import (
    status,
    viewsets
)
from rest_framework.decorators import action
from rest_framework.response import Response

from to_do.models import ToDo
from to_do.serializers.to_do import ToDoSerializer
from to_do.services.to_do import ToDoService


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.order_by('created')
    filterset_fields = (
        'description',
        'title',
        'created'
    )

    def get_queryset(self):
        to_dos = ToDo.objects.filter(
            user_id=self.request.user.id
        ).order_by('created')
        return to_dos

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        to_do = ToDoService.create(serializer.validated_data, request.user)
        return Response(
            self.serializer_class(to_do).data, status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'], url_path='completed')
    def completed(self, request, pk=None):
        to_do = self.get_object()
        ToDoService.completed(to_do)
        return Response(self.serializer_class(to_do).data)
