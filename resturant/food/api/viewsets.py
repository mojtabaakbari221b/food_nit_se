from rest_framework import viewsets
from ..models import Food
from .serializers import FoodSerializer


class FoodViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all().select_related('category')
