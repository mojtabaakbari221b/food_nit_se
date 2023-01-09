from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'name',
            'price',
            'off_percent',
            'views',
            'picture',
            'category',
        ]