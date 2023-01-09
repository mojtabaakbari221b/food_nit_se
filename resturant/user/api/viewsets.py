from django.contrib.auth import get_user_model
from rest_framework import viewsets
from ..models import Cart
from .serializers import UserSerialzier
from .mixins import RetrieveModelViewset


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerialzier
    queryset = get_user_model().objects.all()


class CartViewset(RetrieveModelViewset):
    serializer_class = UserSerialzier
    queryset = Cart.objects.filter(
        is_paid=False,
    ).select_related('user').prefetch_related('foods')