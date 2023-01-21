from rest_framework import serializers


class CartFoodSerializer(serializers.Serializer):
    data = serializers.JSONField()