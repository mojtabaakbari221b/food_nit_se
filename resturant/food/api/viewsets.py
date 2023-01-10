from rest_framework import viewsets
from rest_framework import filters
from url_filter.integrations.drf import DjangoFilterBackend
from ..models import Food
from .serializers import FoodSerializer


class FoodViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all().select_related('category')

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filter_fields = [
        'name',
        'location',
        'category',
    ]

    ordering_fields = [
        'views',
        'off_percent',
        'price',
    ]
