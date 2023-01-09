from rest_framework import serializers
from resturant.food.api.serializers import FoodSerializer
from ..models import User, Food


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
        ]


class CartSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        pass


    class Meta:
        model = Food
        fields = [
            'foods',
            'price',
        ]