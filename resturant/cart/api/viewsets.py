from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Cart
from .serializers import CartSerializer


class CartViewset(viewsets.ReadOnlyModelViewSet):
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