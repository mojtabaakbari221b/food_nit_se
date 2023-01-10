from rest_framework import serializers
from ..models import User


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
        ]


class UserCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
        ]
