from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerialzier, UserCreateSerialzier


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerialzier
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerialzier

        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        readonly_serializer = self.serializer_class(
            serializer.data
        )

        return Response(
            readonly_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
