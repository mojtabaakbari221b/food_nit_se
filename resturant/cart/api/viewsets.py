from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
        ).select_related(
            'user',
        ).prefetch_related(
            'foods',
        )
    
    def list(self, request, *args, **kwargs):
        cart = self.request.user.get_my_cart()
        return self.serializer_class(cart, many=False)