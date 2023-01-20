from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import AuthTokenSerializer


class CustomObtainAuthToken(ViewSet):
    serializer_class = AuthTokenSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})