from rest_framework import serializers
from resturant.food.api.serializers import FoodSerializer
from resturant.food.models import Food


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