from rest_framework import (
    permissions,
    status
)
from rest_framework.response import Response
from rest_framework.views import APIView

from user.services.user import UserService
from user.serializers.user import UserSerializer


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        body = serializer.validated_data
        user = UserService.create(body['username'], body['password'])
        data = self.serializer_class(user).data
        return Response(data, status=status.HTTP_201_CREATED)
