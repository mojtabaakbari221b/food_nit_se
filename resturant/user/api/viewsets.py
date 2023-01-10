from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerialzier


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerialzier
    queryset = get_user_model().objects.all()
