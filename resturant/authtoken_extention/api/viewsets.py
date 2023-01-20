from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AuthTokenSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer