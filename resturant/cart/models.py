from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from resturant.food.models import Food
from .managers import FoodManager


class Cart(models.Model):
    objects = FoodManager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    is_paid = models.BooleanField(
        default=False,
    )

    def get_price_of_items(self, data):
        price = 0

        for food_id, count in data.items() :
            food = get_object_or_404(
                Food.objects.filter(id=food_id)
            )
            price += food.price * count
        
        return price

            
    
    def verify(self):
        self.is_paid = True
        self.save(
            update_fields=[
                'is_paid',
            ],
        )
