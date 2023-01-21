from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from resturant.zarinpal_extention.services import start_transaction

from .serializers import CartFoodSerializer


class CartViewset(viewsets.ViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    
    
    @action(detail=False , methods=["post"])
    def pay(self, request):
        serializer = CartFoodSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)

        user = request.user
        cart = user.get_my_cart()

        cart_amount = cart.get_price_of_items(serializer.data.get('data'))

        result = start_transaction(
            request,
            {
                "user": user,
                "amount": cart_amount,
                "description": "welcome to our shop",
                "mobile": "09111111111",
                "email": user.email,
            }
        )

        return redirect(result)
