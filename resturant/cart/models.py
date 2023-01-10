from django.db import models
from django.conf import settings
from resturant.food.models import Food
from .managers import FoodManager


class Cart(models.Model):
    objects = FoodManager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    foods = models.ManyToManyField(
        Food,
    )

    is_paid = models.BooleanField(
        default=False,
    )

    def get_price_of_items(self):
        price = 0
        for food in self.foods.all():
            price = price + food.price

        return price
    
    def verify(self):
        self.is_paid = True
        self.save(
            update_fields=[
                'is_paid',
            ],
        )
