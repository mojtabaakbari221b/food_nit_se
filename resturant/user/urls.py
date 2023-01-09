from rest_framework.routers import DefaultRouter
from .api import viewsets

router = DefaultRouter()
router.register('', viewsets.UserViewset, basename='user')

urlpatterns = router.urls
