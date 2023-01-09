from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class RetrieveModelViewset(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    pass