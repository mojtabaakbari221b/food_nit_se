from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = get_object_or_404(
                get_user_model().filter(
                    email=email,
                    password=password,
                )
            )
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
