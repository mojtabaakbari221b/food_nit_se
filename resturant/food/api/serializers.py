from rest_framework import serializers
from ..models import Food, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)


    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'price',
            'off_percent',
            'views',
            'picture',
            'category',
        ]