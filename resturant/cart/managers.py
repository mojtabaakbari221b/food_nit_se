from django.contrib.auth.models import BaseUserManager


class FoodManager(BaseUserManager):
    def get_my_cart(self, user):
        query = self.all().prefetch_related('foods__category').get_or_create(
            is_paid=False,
            user=user,
        )

        return query[0]