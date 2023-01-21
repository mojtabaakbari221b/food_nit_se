from django.contrib.auth.models import BaseUserManager


class FoodManager(BaseUserManager):
    def get_my_cart(self, user):
        query = self.get_or_create(
            is_paid=False,
            user=user,
        )

        return query[0]