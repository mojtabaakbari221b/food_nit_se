from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from resturant.zarinpal_extention.services import start_transaction
from ..models import Cart
from .serializers import CartSerializer


class CartViewset(viewsets.GenericViewSet):
    serializer_class = CartSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Cart.objects.get_my_cart(
            user=self.request.user,
        )
    
    def list(self, request, *args, **kwargs):
        user = self.request.user
        cart = user.get_my_cart()

        serializer = self.serializer_class(cart, many=False)

        return Response(serializer.data)
    
    @action(detail=False , methods=["get"])
    def pay(self, request):
        user = request.user
        cart = user.get_my_cart()

        result = start_transaction(
            request,
            {
                "user": user,
                "amount": cart.get_price_of_items(),
                "description": "welcome to our shop",
                "mobile": "09111111111",
                "email": user.email,
            }
        )

        return redirect(result)
