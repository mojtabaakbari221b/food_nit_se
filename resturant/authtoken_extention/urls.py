from rest_framework.routers import DefaultRouter
from .api import viewsets

router = DefaultRouter()
router.register('', viewsets.CustomObtainAuthToken, basename='token')

urlpatterns = router.urls
