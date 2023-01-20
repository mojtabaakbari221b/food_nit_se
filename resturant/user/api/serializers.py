from django.db import IntegrityError
from django.contrib.auth import get_user_model

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
    
    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user
    
    def perform_create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
